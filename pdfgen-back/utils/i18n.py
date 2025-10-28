"""
Internationalization (i18n) module for HasteCV.
Provides translated labels for PDF generation in multiple languages.
"""

# Language translations for PDF section headers and labels
I18N_TRANSLATIONS = {
    'en': {
        'professional_summary': 'PROFESSIONAL SUMMARY',
        'technical_proficiency': 'TECHNICAL PROFICIENCY',
        'professional_experience': 'PROFESSIONAL EXPERIENCE',
        'experience': 'PROFESSIONAL EXPERIENCE',
        'education': 'EDUCATION',
        'projects': 'PROJECTS',
        'skills': 'SKILLS',
        'additional_experience': 'ADDITIONAL EXPERIENCE',
        'position': 'Position',
        'company': 'Company',
        'location': 'Location',
        'dates': 'Dates',
        'degree': 'Degree',
        'institution': 'Institution',
        'responsibilities': 'Responsibilities',
        'technologies': 'Technologies',
        'title': 'Title',
        'url': 'URL',
        'description': 'Description',
    },
    'es': {
        'professional_summary': 'RESUMEN PROFESIONAL',
        'technical_proficiency': 'CONOCIMIENTOS TÉCNICOS',
        'professional_experience': 'EXPERIENCIA PROFESIONAL',
        'experience': 'EXPERIENCIA PROFESIONAL',
        'education': 'EDUCACIÓN',
        'projects': 'PROYECTOS',
        'skills': 'HABILIDADES',
        'additional_experience': 'EXPERIENCIA ADICIONAL',
        'position': 'Puesto',
        'company': 'Empresa',
        'location': 'Ubicación',
        'dates': 'Fechas',
        'degree': 'Título',
        'institution': 'Institución',
        'responsibilities': 'Responsabilidades',
        'technologies': 'Tecnologías',
        'title': 'Título',
        'url': 'URL',
        'description': 'Descripción',
    },
    'fr': {
        'professional_summary': 'RÉSUMÉ PROFESSIONNEL',
        'technical_proficiency': 'COMPÉTENCES TECHNIQUES',
        'professional_experience': 'EXPÉRIENCE PROFESSIONNELLE',
        'experience': 'EXPÉRIENCE PROFESSIONNELLE',
        'education': 'ÉDUCATION',
        'projects': 'PROJETS',
        'skills': 'COMPÉTENCES',
        'additional_experience': 'EXPÉRIENCE SUPPLÉMENTAIRE',
        'position': 'Poste',
        'company': 'Entreprise',
        'location': 'Localisation',
        'dates': 'Dates',
        'degree': 'Diplôme',
        'institution': 'Institution',
        'responsibilities': 'Responsabilités',
        'technologies': 'Technologies',
        'title': 'Titre',
        'url': 'URL',
        'description': 'Description',
    },
    'de': {
        'professional_summary': 'BERUFLICHE ZUSAMMENFASSUNG',
        'technical_proficiency': 'TECHNISCHE FÄHIGKEITEN',
        'professional_experience': 'BERUFSERFAHRUNG',
        'experience': 'BERUFSERFAHRUNG',
        'education': 'AUSBILDUNG',
        'projects': 'PROJEKTE',
        'skills': 'FÄHIGKEITEN',
        'additional_experience': 'ZUSÄTZLICHE ERFAHRUNG',
        'position': 'Position',
        'company': 'Unternehmen',
        'location': 'Standort',
        'dates': 'Daten',
        'degree': 'Abschluss',
        'institution': 'Institution',
        'responsibilities': 'Verantwortungen',
        'technologies': 'Technologien',
        'title': 'Titel',
        'url': 'URL',
        'description': 'Beschreibung',
    },
    'pt': {
        'professional_summary': 'RESUMO PROFISSIONAL',
        'technical_proficiency': 'CONHECIMENTOS TÉCNICOS',
        'professional_experience': 'EXPERIÊNCIA PROFISSIONAL',
        'experience': 'EXPERIÊNCIA PROFISSIONAL',
        'education': 'EDUCAÇÃO',
        'projects': 'PROJETOS',
        'skills': 'HABILIDADES',
        'additional_experience': 'EXPERIÊNCIA ADICIONAL',
        'position': 'Cargo',
        'company': 'Empresa',
        'location': 'Localização',
        'dates': 'Datas',
        'degree': 'Diploma',
        'institution': 'Instituição',
        'responsibilities': 'Responsabilidades',
        'technologies': 'Tecnologias',
        'title': 'Título',
        'url': 'URL',
        'description': 'Descrição',
    }
}

# Supported languages
SUPPORTED_LANGUAGES = list(I18N_TRANSLATIONS.keys())


def get_translation(language, key, default=None):
    """
    Get a translated label for the specified language and key.
    
    Args:
        language: Language code ('en', 'es', 'fr', 'de', 'pt')
        key: Translation key (e.g., 'professional_summary')
        default: Default value if translation not found
    
    Returns:
        Translated text or default value
    """
    if language not in I18N_TRANSLATIONS:
        language = 'en'  # Fallback to English
    
    translations = I18N_TRANSLATIONS[language]
    return translations.get(key, default or key.upper().replace('_', ' '))


def get_all_translations(language):
    """
    Get all translations for a specific language.
    
    Args:
        language: Language code ('en', 'es', 'fr', 'de', 'pt')
    
    Returns:
        Dictionary of all translations for the language
    """
    if language not in I18N_TRANSLATIONS:
        language = 'en'
    
    return I18N_TRANSLATIONS[language]


def is_supported_language(language):
    """
    Check if the language is supported.
    
    Args:
        language: Language code to check
    
    Returns:
        True if language is supported, False otherwise
    """
    return language in SUPPORTED_LANGUAGES
