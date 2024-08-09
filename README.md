# HasteCV

`PyResumeBuilder` is a Python application designed to format and generate a professionally structured resume from a JSON file using the ReportLab library. This application allows you to easily customize and update your resume content in a structured format.

## Features

- Generates a PDF resume from a JSON data file.
- Supports custom fonts and styles.
- Includes sections for contact information, summary, technical proficiency, experience, projects, education, additional experience, and skills.
- Utilizes icons for contact information for a more visually appealing layout.

## Prerequisites

- Python 3.6 or higher
- ReportLab library

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Chrisdalbano/pyresumebuilder.git
   cd pyresumebuilder

2. Create a virtual environment and activate it & install req library:
   ```python
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install reportlab
3. Prepare your JSON:
   ```json
   {
    "name": "",
    "title": "",
    "contact": {
        "email": "",
        "phone": "",
        "location": "",
        "linkedin": "",
        "github": "",
        "website": ""
    },
    "summary": "",
    "technical_proficiency": {
        "languages_frameworks": "",
        "frontend_development": "",
        "backend_development": "",
        "database_technologies": "",
        "devops_cloud": "",
        "tools_platforms": "",
        "testing_debugging": ""
    },
    "experience": [
        {
            "position": "",
            "company": "",
            "location": "",
            "dates": "",
            "responsibilities": [
                ""
            ],
            "technologies": ""
        }
    ],
    "projects": [
        {
            "title": "",
            "url": "",
            "description": "",
            "technologies": ""
        }
    ],
    "education": [
        {
            "degree": "",
            "institution": "",
            "dates": ""
        }
    ],
    "additional_experience": [
        {
            "position": "",
            "company": "",
            "dates": "",
            "responsibilities": [
                ""
            ],
            "technologies": ""
        }
    ],
    "skills": [
        ""
    ]
   }

4. Run the Python file (Make sure you have the json file in the same dir and its named resume_data.json)
   ```sh
   python main.py

Success! Your resume should be generated in PDF at the root of your dir. 


