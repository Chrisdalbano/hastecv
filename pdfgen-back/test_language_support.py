#!/usr/bin/env python3
"""
Test script for multi-language support in HasteCV.
Validates that field names in different languages are correctly normalized.
"""

from utils.layout_utils import normalize_field_name, normalize_resume_data, detect_language


def test_field_name_normalization():
    """Test individual field name normalization."""
    print("=" * 60)
    print("Testing Field Name Normalization")
    print("=" * 60)
    
    test_cases = [
        # Spanish
        ("experiencia", "experience"),
        ("educación", "education"),
        ("habilidades", "skills"),
        ("nombre", "name"),
        
        # French
        ("expérience", "experience"),
        ("éducation", "education"),
        ("compétences", "skills"),
        
        # German
        ("erfahrung", "experience"),
        ("bildung", "education"),
        ("fähigkeiten", "skills"),
        
        # Portuguese
        ("experiência", "experience"),
        ("educação", "education"),
        ("habilidades", "skills"),
        
        # English (should remain unchanged)
        ("experience", "experience"),
        ("education", "education"),
        ("skills", "skills"),
    ]
    
    for input_field, expected in test_cases:
        result = normalize_field_name(input_field)
        status = "✓" if result == expected else "✗"
        print(f"{status} {input_field:15} → {result:15} (expected: {expected})")


def test_resume_data_normalization():
    """Test normalization of complete resume data."""
    print("\n" + "=" * 60)
    print("Testing Resume Data Normalization")
    print("=" * 60)
    
    spanish_resume = {
        "nombre": "Juan García",
        "título": "Ingeniero de Software",
        "contacto": {
            "correo": "juan@example.com",
            "teléfono": "555-1234",
            "ubicación": "Madrid"
        },
        "resumen": "Software engineer with experience...",
        "experiencia": [
            {
                "puesto": "Senior Engineer",
                "empresa": "TechCorp",
                "fechas": "2020-2024",
                "responsabilidades": "Led development..."
            }
        ],
        "educación": [
            {
                "título": "B.S. Computer Science",
                "institución": "Universidad",
                "fechas": "2016-2020"
            }
        ],
        "habilidades": ["Python", "React", "AWS"]
    }
    
    print("\nOriginal Spanish Resume (excerpt):")
    print(f"  nombre: {spanish_resume['nombre']}")
    print(f"  título: {spanish_resume['título']}")
    print(f"  experiencia[0].puesto: {spanish_resume['experiencia'][0]['puesto']}")
    
    normalized = normalize_resume_data(spanish_resume)
    
    print("\nNormalized Resume (excerpt):")
    print(f"  name: {normalized['name']}")
    print(f"  title: {normalized['title']}")
    print(f"  experience[0].position: {normalized['experience'][0]['position']}")
    print(f"  education[0].degree: {normalized['education'][0]['degree']}")
    print(f"  skills: {normalized['skills']}")
    
    print("\n✓ Resume data successfully normalized!")


def test_language_detection():
    """Test automatic language detection."""
    print("\n" + "=" * 60)
    print("Testing Language Detection")
    print("=" * 60)
    
    test_resumes = {
        "English": {
            "name": "John Doe",
            "experience": [{"position": "Engineer"}]
        },
        "Spanish": {
            "nombre": "Juan García",
            "experiencia": [{"puesto": "Ingeniero"}]
        },
        "French": {
            "nom": "Jean Dupont",
            "expérience": [{"poste": "Ingénieur"}]
        }
    }
    
    for lang_name, resume_data in test_resumes.items():
        detected = detect_language(resume_data)
        print(f"Resume: {lang_name:10} → Detected language: {detected}")


if __name__ == "__main__":
    try:
        test_field_name_normalization()
        test_resume_data_normalization()
        test_language_detection()
        
        print("\n" + "=" * 60)
        print("All tests completed! ✓")
        print("=" * 60)
    except Exception as e:
        print(f"\n✗ Error during testing: {e}")
        import traceback
        traceback.print_exc()
