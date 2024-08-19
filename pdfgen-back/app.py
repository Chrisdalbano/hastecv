from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS
from pdf_generator import generate_resume
import json
import logging


app = Flask(__name__, static_folder='dist', template_folder='dist')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        req_data = request.get_json()
        data = req_data.get('data')
        template = req_data.get('template', 'default')

        # Parse the data if it's a JSON string
        if isinstance(data, str):
            data = json.loads(data)

        # Validate the data
        if not data or not isinstance(data, dict):
            raise ValueError("Invalid data format")

        # Generate the PDF resume with the specified template
        generate_resume(data, template=template)

        # Send the generated PDF file as a response
        return send_file('resume.pdf', as_attachment=True)

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/templates')
def get_templates():
    templates = ["default", "modern", "minimal"]
    return jsonify(templates)

@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)

if __name__ == "__main__":
    app.run(debug=True)
