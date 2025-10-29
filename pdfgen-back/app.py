import sys
import os
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from flask_talisman import Talisman
import json
import logging

# Add the current project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    # Try to import new generator first
    from pdf_generator_v2 import generate_resume
    using_v2 = True
except ImportError:
    # Fall back to legacy generator
    from pdf_generator import generate_resume
    using_v2 = False

# Import language normalization utilities
from utils.layout_utils import normalize_resume_data
from utils.i18n import get_translation, is_supported_language

# Initialize Flask app
app = Flask(__name__)

# Set default configurations
app.config.from_mapping(
    ENV=os.getenv("FLASK_ENV", "production"),  # Default to production
    DEBUG=os.getenv("FLASK_DEBUG", False),  # Default debug setting
)

# CORS Configuration based on environment
def configure_cors():
    """Configure CORS based on the environment."""
    env = app.config["ENV"]
    
    if env == "production":
        # Production settings: Allow CORS only for production frontend domain
        # Support both www and non-www versions, and different subdomains
        prod_origins = [
            "https://www.hastecv.com",
            "https://hastecv.com",
            "https://app.hastecv.com",
            os.getenv("FRONTEND_DOMAIN", "https://www.hastecv.com")
        ]
        
        cors_config = {
            "resources": {r"/*": {
                "origins": prod_origins,
                "methods": ["GET", "POST", "OPTIONS"],
                "allow_headers": [
                    "Content-Type", 
                    "Authorization",
                    "Accept",
                    "Origin"
                ],
                "expose_headers": [
                    "Content-Type", 
                    "Content-Disposition"
                ],
                "supports_credentials": True,
                "max_age": 3600
            }}
        }
        
        app.logger.info(f"CORS Production Config - Allowed origins: {prod_origins}")
    else:
        # Development settings - Allow localhost and 127.0.0.1 with all common ports
        local_origins = [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
            "http://localhost:8080",
            "http://127.0.0.1:8080",
            "http://localhost:5174",
            "http://127.0.0.1:5174",
            "http://localhost",
            "http://127.0.0.1",
        ]
        
        # Allow custom origin from environment variable for flexibility
        custom_origin = os.getenv("CORS_ORIGINS")
        if custom_origin:
            local_origins.extend(custom_origin.split(","))
        
        cors_config = {
            "resources": {r"/*": {
                "origins": local_origins,
                "methods": ["GET", "POST", "OPTIONS", "PUT", "DELETE"],
                "allow_headers": [
                    "Content-Type", 
                    "Authorization",
                    "Accept",
                    "Origin",
                    "X-Requested-With"
                ],
                "expose_headers": ["Content-Type", "Content-Disposition"],
                "supports_credentials": True,
                "max_age": 3600
            }}
        }
        
        app.logger.info(f"CORS Development Config - Allowed origins: {', '.join(local_origins)}")
    
    CORS(app, **cors_config)

# Configure CORS
configure_cors()

# Configure Talisman (security headers) - Must allow CORS to work
if app.config["ENV"] == "production":
    # Production: HTTPS enforcement enabled, but allow CORS
    Talisman(app, 
             force_https=True,
             strict_transport_security=True,
             content_security_policy=None,  # Let after_request handle CSP
             session_cookie_secure=True)
else:
    # Development: Minimal security for local testing
    Talisman(app, 
             force_https=False,
             content_security_policy=None)

# Setup logging
handler = logging.StreamHandler()
handler.setLevel(logging.ERROR)
app.logger.addHandler(handler)


# API functionality here
@app.route("/generate", methods=["POST", "OPTIONS"])
def generate():
    # Handle CORS preflight requests
    if request.method == "OPTIONS":
        return "", 204
    
    try:
        req_data = request.get_json()
        data = req_data.get("data")
        template = req_data.get("template", "default")
        language = req_data.get("language", "en")  # Get language from request

        if isinstance(data, str):
            data = json.loads(data)

        if not data or not isinstance(data, dict):
            raise ValueError("Invalid data format")
        
        # Validate language
        if not is_supported_language(language):
            language = "en"
        
        # Normalize field names to support multiple languages
        data = normalize_resume_data(data)

        # Call the resume generation function with language
        generate_resume(data, template=template, language=language)
        return send_file("resume.pdf", as_attachment=True)

    except ValueError as ve:
        app.logger.error(f"ValueError: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


# Secure headers for all responses (CORS is handled by Flask-CORS extension)
@app.after_request
def set_secure_headers(response):
    # DO NOT manually set CORS headers - Flask-CORS handles this automatically
    # Manual headers can interfere with preflight responses
    
    response.headers["Content-Security-Policy"] = "default-src 'self';"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    
    return response


@app.route("/templates")
def get_templates():
    """Get available resume templates with descriptions."""
    if using_v2:
        from pdf_generator_v2 import get_available_templates
        templates_config = get_available_templates()
        
        # Format for frontend
        templates = []
        for name, config in templates_config.items():
            templates.append({
                'id': name,
                'name': name.title(),
                'description': config['description'],
                'features': config['features'],
                'layout': config['layout']
            })
        
        return jsonify(templates)
    else:
        # Legacy response
        templates = ["default", "modern", "minimal"]
        return jsonify(templates)


@app.route("/generate-visual", methods=["POST", "OPTIONS"])
def generate_visual():
    """Generate PDF from visual layout configuration."""
    # Handle CORS preflight requests
    if request.method == "OPTIONS":
        return "", 204
    
    try:
        req_data = request.get_json()
        layout_config = req_data.get('layout')
        resume_data = req_data.get('data')
        filename = req_data.get('filename', 'resume')
        language = req_data.get('language', 'en')  # Get language from request
        
        if not layout_config or not resume_data:
            raise ValueError("Missing layout or data")
        
        # Validate language
        if not is_supported_language(language):
            language = 'en'
        
        # Normalize field names to support multiple languages
        resume_data = normalize_resume_data(resume_data)
        
        # Import visual layout generator
        from layouts.visual_layout import generate_visual_layout
        
        # Generate PDF
        output_file = f'{filename}.pdf' if not filename.endswith('.pdf') else filename
        generate_visual_layout(resume_data, layout_config, output_file)
        
        return send_file(output_file, as_attachment=True)
        
    except ValueError as ve:
        app.logger.error(f"ValueError: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        app.logger.error(f"Unexpected error in generate_visual: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


# Health check endpoint for monitoring
@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "environment": app.config["ENV"],
        "generator": "v2" if using_v2 else "legacy"
    }), 200


if __name__ == "__main__":
    # Print environment information
    print("\n" + "="*50)
    print(f"Flask Environment: {app.config['ENV']}")
    print(f"Debug Mode: {app.config['DEBUG']}")
    print("="*50 + "\n")
    
    # Run Flask app with debug mode if in development
    app.run(debug=app.config["DEBUG"])
