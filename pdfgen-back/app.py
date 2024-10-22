import sys
import os
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from flask_talisman import Talisman
import json
import logging

# Add the current project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from .pdf_generator import generate_resume

# Initialize Flask app
app = Flask(__name__)

# Set default configurations
app.config.from_mapping(
    ENV=os.getenv("FLASK_ENV", "production"),  # Default to production
    DEBUG=os.getenv("FLASK_DEBUG", False)      # Default debug setting
)

# Safely configure CORS and Talisman based on the environment
if app.config["ENV"] == "production":
    # Production settings
    CORS(app, resources={r"/*": {"origins": "https://www.hastecv.com"}})
    Talisman(app)  # Enable HTTPS enforcement in production
else:
    # Development settings
    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
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

@app.route("/templates")
def get_templates():
    templates = ["default", "modern", "minimal"]
    return jsonify(templates)

# Secure headers for all responses
@app.after_request
def set_secure_headers(response):
    response.headers["Content-Security-Policy"] = "default-src 'self';"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    return response

if __name__ == "__main__":
    # Run Flask app with debug mode if in development
    app.run(debug=app.config["DEBUG"])
