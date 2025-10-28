from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle

"""
Language and field normalization utilities for multi-language support.
"""

# Language field mappings
LANGUAGE_FIELD_MAPPINGS = {
    'en': {
        'name': ['name'],
        'title': ['title', 'job_title', 'position'],
        'contact': ['contact'],
        'email': ['email'],
        'phone': ['phone'],
        'location': ['location'],
        'website': ['website', 'web', 'url'],
        'github': ['github'],
        'linkedin': ['linkedin'],
        'summary': ['summary', 'professional_summary', 'bio'],
        'experience': ['experience', 'work_experience', 'employment'],
        'education': ['education', 'academic'],
        'skills': ['skills', 'competencies', 'technical_proficiency'],
        'projects': ['projects', 'portfolio'],
        'additional_experience': ['additional_experience', 'other_experience'],
    },
    'es': {
        'name': ['nombre'],
        'title': ['título', 'cargo', 'puesto'],
        'contact': ['contacto'],
        'email': ['correo', 'email'],
        'phone': ['teléfono', 'telefono', 'celular', 'móvil'],
        'location': ['ubicación', 'ciudad', 'localización'],
        'website': ['sitio_web', 'sitio web', 'web', 'página', 'url'],
        'github': ['github'],
        'linkedin': ['linkedin'],
        'summary': ['resumen', 'resumen_profesional', 'biografía', 'bio'],
        'experience': ['experiencia', 'experiencia_laboral', 'empleo'],
        'education': ['educación', 'estudios', 'formación'],
        'skills': ['habilidades', 'competencias', 'destrezas'],
        'projects': ['proyectos', 'portafolio'],
        'additional_experience': ['experiencia_adicional', 'otra_experiencia'],
    },
    'fr': {
        'name': ['nom', 'prénom'],
        'title': ['titre', 'poste', 'fonction'],
        'contact': ['contact'],
        'email': ['email', 'courriel'],
        'phone': ['téléphone', 'telephone', 'mobile'],
        'location': ['localisation', 'emplacement', 'ville'],
        'website': ['site_web', 'site', 'web', 'url'],
        'github': ['github'],
        'linkedin': ['linkedin'],
        'summary': ['résumé', 'resume', 'biographie', 'bio'],
        'experience': ['expérience', 'experience', 'emploi'],
        'education': ['éducation', 'education', 'formation'],
        'skills': ['compétences', 'competences', 'habilités'],
        'projects': ['projets', 'portefeuille'],
        'additional_experience': ['expérience_supplémentaire', 'experience_supplementaire'],
    },
    'de': {
        'name': ['name', 'namen'],
        'title': ['titel', 'position', 'beruf'],
        'contact': ['kontakt'],
        'email': ['email', 'e-mail'],
        'phone': ['telefon', 'handy'],
        'location': ['ort', 'standort', 'stadt'],
        'website': ['website', 'webseite', 'url'],
        'github': ['github'],
        'linkedin': ['linkedin'],
        'summary': ['zusammenfassung', 'bio', 'profil'],
        'experience': ['erfahrung', 'berufserfahrung', 'arbeit'],
        'education': ['bildung', 'ausbildung', 'schulung'],
        'skills': ['fähigkeiten', 'kompetenzen', 'fertigkeiten'],
        'projects': ['projekte', 'portfolio'],
        'additional_experience': ['weitere_erfahrung', 'zusatzlicheerfahrung'],
    },
    'pt': {
        'name': ['nome'],
        'title': ['título', 'cargo', 'posição'],
        'contact': ['contato'],
        'email': ['email', 'correio'],
        'phone': ['telefone', 'celular', 'móvel'],
        'location': ['localização', 'localiza', 'cidade'],
        'website': ['site', 'web', 'url', 'página'],
        'github': ['github'],
        'linkedin': ['linkedin'],
        'summary': ['resumo', 'resumo_profissional', 'biografia', 'bio'],
        'experience': ['experiência', 'experiencia', 'emprego'],
        'education': ['educação', 'educacao', 'formação'],
        'skills': ['habilidades', 'competências', 'destrezas'],
        'projects': ['projetos', 'portfólio'],
        'additional_experience': ['experiência_adicional', 'experiencia_adicional'],
    }
}

# Reverse mapping for easy lookup
FIELD_TO_LANGUAGE = {}
for lang, fields in LANGUAGE_FIELD_MAPPINGS.items():
    for standard_field, variants in fields.items():
        for variant in variants:
            variant_lower = variant.lower()
            if variant_lower not in FIELD_TO_LANGUAGE:
                FIELD_TO_LANGUAGE[variant_lower] = standard_field


def normalize_field_name(field_name):
    """
    Convert a field name (potentially in any language) to the standard English field name.
    
    Args:
        field_name: The field name to normalize (string)
    
    Returns:
        The standard English field name, or the original if not found
    """
    if isinstance(field_name, str):
        field_lower = field_name.lower().strip()
        return FIELD_TO_LANGUAGE.get(field_lower, field_name)
    return field_name


def normalize_resume_data(data):
    """
    Normalize all field names in resume data to standard English names.
    
    Args:
        data: Resume data dictionary (potentially with field names in any language)
    
    Returns:
        Normalized resume data with all standard English field names
    """
    if not isinstance(data, dict):
        return data
    
    normalized = {}
    
    for key, value in data.items():
        standard_key = normalize_field_name(key)
        
        # Handle nested dictionaries (like contact info)
        if isinstance(value, dict):
            normalized[standard_key] = {
                normalize_field_name(k): v for k, v in value.items()
            }
        # Handle lists of dictionaries (like experience, education)
        elif isinstance(value, list) and value and isinstance(value[0], dict):
            normalized[standard_key] = [
                {normalize_field_name(k): v for k, v in item.items()}
                for item in value
            ]
        else:
            normalized[standard_key] = value
    
    return normalized


def detect_language(data):
    """
    Attempt to detect the language of the resume data based on field names.
    
    Args:
        data: Resume data dictionary
    
    Returns:
        Detected language code ('en', 'es', etc.) or 'en' as default
    """
    if not isinstance(data, dict):
        return 'en'
    
    # Get all field names
    field_names = set()
    
    def collect_fields(obj):
        if isinstance(obj, dict):
            field_names.update(obj.keys())
            for v in obj.values():
                if isinstance(v, (dict, list)):
                    collect_fields(v)
        elif isinstance(obj, list):
            for item in obj:
                if isinstance(item, dict):
                    collect_fields(item)
    
    collect_fields(data)
    
    # Count matches for each language
    language_scores = {lang: 0 for lang in LANGUAGE_FIELD_MAPPINGS.keys()}
    
    for field in field_names:
        field_lower = field.lower()
        for lang, field_mappings in LANGUAGE_FIELD_MAPPINGS.items():
            for variants in field_mappings.values():
                if field_lower in [v.lower() for v in variants]:
                    language_scores[lang] += 1
                    break
    
    # Return language with highest score, default to 'en'
    best_language = max(language_scores, key=language_scores.get)
    return best_language if language_scores[best_language] > 0 else 'en'


def create_contact_table(contact_data, icon_size, styles):
    contact_grid_data = []
    for i in range(0, len(contact_data), 2):
        if i + 1 < len(contact_data):
            contact_grid_data.append(contact_data[i] + contact_data[i + 1])
        else:
            contact_grid_data.append(contact_data[i])

    contact_table = Table(contact_grid_data, hAlign='CENTER', colWidths=[icon_size, 6, 2.4 * inch, icon_size, 6, 2.4 * inch])
    contact_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'OpenSans-Regular'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))

    return contact_table
