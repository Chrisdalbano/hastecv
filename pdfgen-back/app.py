from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS
from pdf_generator import generate_resume
from flask_talisman import Talisman
import json
import logging


app = Flask(__name__, static_folder='dist', template_folder='dist')
CORS(app, resources={r"/generate": {"origins": "https://hastecv.com"}})
Talisman(app)

# Setup logging
handler = logging.StreamHandler()
handler.setLevel(logging.ERROR)
app.logger.addHandler(handler)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    try:
        req_data = request.get_json()
        data = req_data.get('data')
        template = req_data.get('template', 'default')

        if isinstance(data, str):
            data = json.loads(data)

        if not data or not isinstance(data, dict):
            raise ValueError("Invalid data format")

        generate_resume(data, template=template)
        return send_file('resume.pdf', as_attachment=True)

    except ValueError as ve:
        app.logger.error(f"ValueError: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500


@app.route('/templates')
def get_templates():
    templates = ["default", "modern", "minimal"]
    return jsonify(templates)


@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


@app.after_request
def set_secure_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self';"
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    return response


if __name__ == "__main__":
    app.run(debug=False)
