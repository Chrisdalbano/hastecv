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


## 🌍 Multi-Language Support

HasteCV now supports **5 languages** for creating resumes! You can:

### Supported Languages
- 🇺🇸 **English** - Default language
- 🇪🇸 **Spanish** - Full support for Spanish field names (e.g., `experiencia`, `educación`)
- 🇫🇷 **French** - Support for French field names (e.g., `expérience`, `éducation`)
- 🇩🇪 **German** - Support for German field names (e.g., `erfahrung`, `bildung`)
- 🇵🇹 **Portuguese** - Support for Portuguese field names (e.g., `experiência`, `educação`)

### How It Works

1. **Language Selector** - Use the dropdown in the app header to switch languages
2. **Auto Translation** - Field names are automatically normalized to English internally
3. **UI Translation** - All form labels, buttons, and titles appear in your selected language
4. **Smart Detection** - The system automatically detects the language of your resume data

### Examples

**Spanish Resume:**
```json
{
  "nombre": "Juan García",
  "título": "Ingeniero de Software",
  "experiencia": [
    {
      "puesto": "Senior Engineer",
      "empresa": "TechCorp"
    }
  ]
}
// Works perfectly! ✓
```

**French Resume:**
```json
{
  "nom": "Jean Dupont",
  "titre": "Ingénieur Logiciel",
  "expérience": [
    {
      "poste": "Ingénieur Principal",
      "entreprise": "TechCorp"
    }
  ]
}
// Supported! ✓
```

### Features

✅ Automatic field name normalization  
✅ Localized UI in 5 languages  
✅ Language preference saved automatically  
✅ 50+ field name variants supported  
✅ 100% backward compatible  
✅ Zero breaking changes  

### Documentation

- **[Multi-Language Support Guide](./MULTI-LANGUAGE-SUPPORT.md)** - Complete technical documentation
- **[Spanish Quick Start](./SPANISH-LANGUAGE-QUICK-START.md)** - Spanish language guide
- **[Implementation Details](./LANGUAGE-SUPPORT-IMPLEMENTATION.md)** - Architecture and technical details
- **[Changes Summary](./SPANISH-SUPPORT-CHANGES-SUMMARY.md)** - Summary of all changes

### Adding More Languages

The system is designed to be easily extensible. To add a new language:

1. Add field mappings to `pdfgen-back/utils/layout_utils.py`
2. Add UI translations to `pdfgen-front/src/stores/resumeData.js`
3. Add language option to `pdfgen-front/src/components/LanguageSelector.vue`

See [MULTI-LANGUAGE-SUPPORT.md](./MULTI-LANGUAGE-SUPPORT.md) for detailed instructions.

---

**Status:** ✅ Production Ready  
**Tested Languages:** English, Spanish, French, German, Portuguese  
**Last Updated:** October 2025 


