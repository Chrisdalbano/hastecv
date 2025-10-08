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

# Initialize Flask app
app = Flask(__name__)

# Set default configurations
app.config.from_mapping(
    ENV=os.getenv("FLASK_ENV", "production"),  # Default to production
    DEBUG=os.getenv("FLASK_DEBUG", False),  # Default debug setting
)

# Safely configure CORS and Talisman based on the environment
if app.config["ENV"] == "production":
    # Production settings: Allow CORS for the production frontend domain
    CORS(
        app,
        resources={r"/*": {"origins": "https://www.hastecv.com"}},
        supports_credentials=True,
    )
    Talisman(app)  # Enable HTTPS enforcement in production
else:
    # Development settings - allow both localhost and 127.0.0.1
    CORS(
        app,
        resources={r"/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}},
        supports_credentials=True,
    )
    Talisman(app, force_https=False)  # Disable HTTPS enforcement for local dev

# Setup logging
handler = logging.StreamHandler()
handler.setLevel(logging.ERROR)
app.logger.addHandler(handler)


# API functionality here
@app.route("/generate", methods=["POST"])
def generate():
    try:
        req_data = request.get_json()
        data = req_data.get("data")
        template = req_data.get("template", "default")

        if isinstance(data, str):
            data = json.loads(data)

        if not data or not isinstance(data, dict):
            raise ValueError("Invalid data format")

        # Call the resume generation function
        generate_resume(data, template=template)
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
    response.headers["Content-Security-Policy"] = "default-src 'self';"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    
    # Note: CORS headers are automatically added by Flask-CORS extension
    # Do not manually add CORS headers here to avoid duplicates
    
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


@app.route("/generate-visual", methods=["POST"])
def generate_visual():
    """Generate PDF from visual layout configuration."""
    try:
        req_data = request.get_json()
        layout_config = req_data.get('layout')
        resume_data = req_data.get('data')
        filename = req_data.get('filename', 'resume')
        
        if not layout_config or not resume_data:
            raise ValueError("Missing layout or data")
        
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


if __name__ == "__main__":
    # Print environment information
    print("\n" + "="*50)
    print(f"Flask Environment: {app.config['ENV']}")
    print(f"Debug Mode: {app.config['DEBUG']}")
    print("="*50 + "\n")
    
    # Run Flask app with debug mode if in development
    app.run(debug=app.config["DEBUG"])
