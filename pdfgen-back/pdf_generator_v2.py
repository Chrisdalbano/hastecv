"""
Modern, professional PDF resume generator.
Refactored for better space utilization, professional designs, and ATS compliance.
"""
import os
from styles.professional_styles import get_professional_styles, get_template_colors
from layouts.single_column import generate_single_column_resume
from layouts.two_column import generate_two_column_resume


# Template configuration
TEMPLATE_CONFIG = {
    'executive': {
        'layout': 'single_column',
        'density': 'balanced',
        'description': 'Traditional single-column layout with professional navy theme. Perfect for corporate roles.',
        'features': ['Single column', 'Professional colors', 'Clear hierarchy', 'ATS-optimized']
    },
    'technical': {
        'layout': 'two_column',
        'density': 'compact',
        'description': 'Two-column layout with skills sidebar. Ideal for technical and engineering roles.',
        'features': ['Two columns', 'Skills sidebar', 'Compact design', 'Technical focus']
    },
    'modern': {
        'layout': 'single_column',
        'density': 'balanced',
        'description': 'Clean, modern design with contemporary colors. Great for creative and modern companies.',
        'features': ['Modern aesthetic', 'Blue accents', 'Balanced spacing', 'Contemporary']
    },
    'compact': {
        'layout': 'single_column',
        'density': 'compact',
        'description': 'Maximum content density without looking cramped. Best for experienced professionals.',
        'features': ['High density', 'More content per page', 'Professional', 'Efficient']
    },
    'creative': {
        'layout': 'single_column',
        'density': 'balanced',
        'description': 'Bold, eye-catching design with Riot Games-inspired aesthetics. Perfect for game design and creative tech roles.',
        'features': ['Bold red accents', 'Gold highlights', 'Gaming industry', 'Creative & modern']
    },
    # Legacy templates mapped to new system
    'default': {
        'layout': 'single_column',
        'density': 'balanced',
        'description': 'Classic professional layout (legacy support).',
        'features': ['Traditional', 'Professional', 'ATS-friendly', 'Classic']
    },
    'minimal': {
        'layout': 'single_column',
        'density': 'balanced',
        'description': 'Minimalist design (legacy support).',
        'features': ['Minimal', 'Clean', 'Simple', 'Elegant']
    }
}


def generate_resume(data, template='executive', output_file='resume.pdf'):
    """
    Generate a professional resume PDF.
    
    Args:
        data: Resume data dictionary with sections like name, experience, education, etc.
        template: Template name ('executive', 'technical', 'modern', 'compact')
        output_file: Output filename for the generated PDF
    
    Returns:
        Path to the generated PDF file
    """
    # Get template configuration
    template_config = TEMPLATE_CONFIG.get(template, TEMPLATE_CONFIG['executive'])
    layout_type = template_config['layout']
    density = template_config['density']
    
    # Map legacy template names to new ones
    template_map = {
        'default': 'executive',
        'minimal': 'modern'
    }
    display_template = template_map.get(template, template)
    
    # Get styles for this template
    styles = get_professional_styles(template=display_template, density=density)
    
    # Generate based on layout type
    if layout_type == 'two_column':
        return generate_two_column_resume(
            data=data,
            styles=styles,
            template=display_template,
            density=density,
            output_file=output_file
        )
    else:  # single_column
        return generate_single_column_resume(
            data=data,
            styles=styles,
            template=display_template,
            density=density,
            output_file=output_file
        )


def get_available_templates():
    """
    Get list of available templates with descriptions.
    
    Returns:
        Dictionary of template configurations
    """
    return TEMPLATE_CONFIG


def get_template_info(template='executive'):
    """
    Get detailed information about a specific template.
    
    Args:
        template: Template name
    
    Returns:
        Dictionary with template configuration
    """
    return TEMPLATE_CONFIG.get(template, TEMPLATE_CONFIG['executive'])


# For backward compatibility with old code
def generate_resume_legacy(data, template="minimal"):
    """
    Legacy function signature for backward compatibility.
    Redirects to new generate_resume function.
    """
    return generate_resume(data, template=template)


if __name__ == "__main__":
    # Test with sample data
    sample_data = {
        "name": "John Doe",
        "title": "Senior Software Engineer",
        "contact": {
            "email": "john.doe@email.com",
            "phone": "555-123-4567",
            "location": "San Francisco, CA",
            "linkedin": "https://linkedin.com/in/johndoe",
            "github": "https://github.com/johndoe",
            "website": "https://johndoe.dev"
        },
        "summary": "Experienced software engineer with 8+ years building scalable web applications. Specialized in full-stack development with React, Node.js, and cloud infrastructure. Proven track record of leading technical teams and delivering high-impact projects.",
        "technical_proficiency": {
            "languages": "JavaScript, TypeScript, Python, Go",
            "frontend": "React, Vue.js, Next.js, Tailwind CSS",
            "backend": "Node.js, Express, Django, FastAPI",
            "databases": "PostgreSQL, MongoDB, Redis",
            "cloud": "AWS, Docker, Kubernetes, CI/CD"
        },
        "experience": [
            {
                "position": "Senior Software Engineer",
                "company": "TechCorp",
                "location": "San Francisco, CA",
                "dates": "2020 - Present",
                "responsibilities": [
                    "Led development of microservices architecture serving 5M+ users",
                    "Reduced API response time by 60% through optimization",
                    "Mentored team of 5 junior engineers",
                    "Implemented CI/CD pipeline reducing deployment time by 80%"
                ],
                "technologies": "React, Node.js, PostgreSQL, AWS, Docker"
            }
        ],
        "education": [
            {
                "degree": "B.S. Computer Science",
                "institution": "University of California",
                "dates": "2012 - 2016"
            }
        ],
        "skills": [
            "Full-Stack Development",
            "System Architecture",
            "Team Leadership",
            "Agile/Scrum",
            "Code Review",
            "Performance Optimization"
        ]
    }
    
    # Generate test resumes
    for template_name in ['executive', 'technical', 'modern', 'compact']:
        output = f"test_resume_{template_name}.pdf"
        generate_resume(sample_data, template=template_name, output_file=output)
        print(f"Generated: {output}")

