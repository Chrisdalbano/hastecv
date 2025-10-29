"""
Professional, modern styles for resume templates.
Optimized for space efficiency and visual hierarchy.
"""
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib import colors
from styles.fonts import register_fonts


def get_professional_styles(template='executive', density='balanced', primary_color=None):
    """
    Get optimized professional styles for resume generation.
    
    Args:
        template: Template name ('executive', 'technical', 'modern', 'compact')
        density: Spacing density ('compact', 'balanced', 'spacious')
        primary_color: Optional hex color code to override template color (e.g., '#1E3A8A')
    
    Returns:
        Dictionary of ParagraphStyle objects
    """
    register_fonts()
    
    # Base font sizes - adjust based on density
    size_multiplier = {
        'compact': 0.95,
        'balanced': 1.0,
        'spacious': 1.05
    }.get(density, 1.0)
    
    # Color schemes for different templates
    color_schemes = {
        'executive': {
            'primary': colors.HexColor('#1a365d'),  # Navy blue
            'secondary': colors.HexColor('#2c5282'),  # Lighter navy
            'accent': colors.HexColor('#4a5568'),  # Slate gray
            'text': colors.HexColor('#1a202c'),  # Near black
            'link': colors.HexColor('#2b6cb0')  # Professional blue
        },
        'technical': {
            'primary': colors.HexColor('#2d3748'),  # Dark gray
            'secondary': colors.HexColor('#4a5568'),  # Medium gray
            'accent': colors.HexColor('#3182ce'),  # Blue
            'text': colors.HexColor('#1a202c'),
            'link': colors.HexColor('#3182ce')
        },
        'modern': {
            'primary': colors.HexColor('#2d3748'),
            'secondary': colors.HexColor('#63b3ed'),  # Sky blue
            'accent': colors.HexColor('#4299e1'),  # Bright blue
            'text': colors.HexColor('#2d3748'),
            'link': colors.HexColor('#3182ce')
        },
        'compact': {
            'primary': colors.HexColor('#000000'),  # Black
            'secondary': colors.HexColor('#4a5568'),  # Gray
            'accent': colors.HexColor('#718096'),  # Light gray
            'text': colors.HexColor('#1a202c'),
            'link': colors.HexColor('#2c5282')
        },
        'creative': {
            'primary': colors.HexColor('#D13639'),  # Riot Red
            'secondary': colors.HexColor('#1E1E1E'),  # Near black
            'accent': colors.HexColor('#C28F2C'),  # Gold accent
            'text': colors.HexColor('#1E1E1E'),  # Near black
            'link': colors.HexColor('#D13639'),  # Riot Red
            'highlight': colors.HexColor('#F0E6D2')  # Cream/Gold highlight
        }
    }
    
    colors_dict = color_schemes.get(template, color_schemes['executive'])
    
    # Override primary color if custom color is provided
    if primary_color:
        try:
            # Parse hex color and override primary colors
            custom_color = colors.HexColor(primary_color)
            colors_dict['primary'] = custom_color
            colors_dict['secondary'] = custom_color  # Also apply to secondary for consistency
            colors_dict['link'] = custom_color
            colors_dict['accent'] = custom_color  # And accent colors
            # Keep text color as-is for readability
        except Exception as e:
            # If invalid color, log and continue with template default
            print(f"Invalid primary_color '{primary_color}': {e}")
    
    # Define all styles
    styles = {}
    
    # Name - Large, bold, attention-grabbing
    styles['Name'] = ParagraphStyle(
        'Name',
        fontName='Lexend-Bold',
        fontSize=int(22 * size_multiplier),
        leading=int(26 * size_multiplier),
        textColor=colors_dict['primary'],
        spaceAfter=0,
        alignment=TA_LEFT
    )
    
    # Title/Role - Professional subtitle
    styles['Title'] = ParagraphStyle(
        'Title',
        fontName='OpenSans-Regular',
        fontSize=int(11 * size_multiplier),
        leading=int(13 * size_multiplier),
        textColor=colors_dict['secondary'],
        spaceAfter=0,
        alignment=TA_LEFT
    )
    
    # Contact information - Compact, single line
    styles['Contact'] = ParagraphStyle(
        'Contact',
        fontName='OpenSans-Regular',
        fontSize=int(9 * size_multiplier),
        leading=int(11 * size_multiplier),
        textColor=colors_dict['text'],
        spaceAfter=0,
        alignment=TA_LEFT
    )
    
    # Section headers - Clear hierarchy
    styles['SectionHeader'] = ParagraphStyle(
        'SectionHeader',
        fontName='OpenSans-Bold',
        fontSize=int(12 * size_multiplier),
        leading=int(14 * size_multiplier),
        textColor=colors_dict['primary'],
        spaceAfter=2,
        spaceBefore=0,
        alignment=TA_LEFT,
        borderPadding=0
    )
    
    # Job header - Position, company, dates (MORE BOLD AND PROMINENT)
    styles['JobHeader'] = ParagraphStyle(
        'JobHeader',
        fontName='OpenSans-Bold',
        fontSize=int(10.5 * size_multiplier),
        leading=int(13 * size_multiplier),
        textColor=colors_dict['text'],
        spaceAfter=0,
        alignment=TA_LEFT
    )
    
    # Body text - Main content
    styles['BodyText'] = ParagraphStyle(
        'BodyText',
        fontName='OpenSans-Regular',
        fontSize=int(9.5 * size_multiplier),
        leading=int(11 * size_multiplier),
        textColor=colors_dict['text'],
        spaceAfter=0,
        alignment=TA_JUSTIFY
    )
    
    # Bullet text - Experience bullets
    styles['BulletText'] = ParagraphStyle(
        'BulletText',
        fontName='OpenSans-Regular',
        fontSize=int(9 * size_multiplier),
        leading=int(10.5 * size_multiplier),
        textColor=colors_dict['text'],
        leftIndent=5,
        spaceAfter=0,
        alignment=TA_LEFT
    )
    
    # Technical proficiency text
    styles['TechProfText'] = ParagraphStyle(
        'TechProfText',
        fontName='OpenSans-Regular',
        fontSize=int(9 * size_multiplier),
        leading=int(11 * size_multiplier),
        textColor=colors_dict['text'],
        spaceAfter=0,
        alignment=TA_LEFT
    )
    
    # Skills text - Inline format
    styles['SkillsText'] = ParagraphStyle(
        'SkillsText',
        fontName='OpenSans-Regular',
        fontSize=int(9 * size_multiplier),
        leading=int(11 * size_multiplier),
        textColor=colors_dict['text'],
        spaceAfter=0,
        alignment=TA_LEFT
    )
    
    # Technology text - Italicized
    styles['TechText'] = ParagraphStyle(
        'TechText',
        fontName='OpenSans-Italic',
        fontSize=int(8.5 * size_multiplier),
        leading=int(10 * size_multiplier),
        textColor=colors_dict['accent'],
        spaceAfter=0,
        alignment=TA_LEFT
    )
    
    # Project title
    styles['ProjectTitle'] = ParagraphStyle(
        'ProjectTitle',
        fontName='OpenSans-Bold',
        fontSize=int(10 * size_multiplier),
        leading=int(12 * size_multiplier),
        textColor=colors_dict['primary'],
        spaceAfter=0,
        alignment=TA_LEFT
    )
    
    # Project description
    styles['ProjectDesc'] = ParagraphStyle(
        'ProjectDesc',
        fontName='OpenSans-Regular',
        fontSize=int(9 * size_multiplier),
        leading=int(10.5 * size_multiplier),
        textColor=colors_dict['text'],
        spaceAfter=0,
        alignment=TA_LEFT
    )
    
    # Education text
    styles['EducationText'] = ParagraphStyle(
        'EducationText',
        fontName='OpenSans-Regular',
        fontSize=int(9.5 * size_multiplier),
        leading=int(11 * size_multiplier),
        textColor=colors_dict['text'],
        spaceAfter=0,
        alignment=TA_LEFT
    )
    
    # Store color scheme in styles dict for reference
    styles['_colors'] = colors_dict
    
    return styles


def get_template_colors(template='executive'):
    """
    Get color scheme for a specific template.
    
    Args:
        template: Template name
    
    Returns:
        Dictionary of color values
    """
    color_schemes = {
        'executive': {
            'header_bg': colors.HexColor('#1a365d'),
            'header_text': colors.white,
            'section_line': colors.HexColor('#cbd5e0'),
            'accent': colors.HexColor('#2c5282')
        },
        'technical': {
            'header_bg': colors.HexColor('#2d3748'),
            'header_text': colors.white,
            'section_line': colors.HexColor('#3182ce'),
            'accent': colors.HexColor('#3182ce')
        },
        'modern': {
            'header_bg': colors.white,
            'header_text': colors.HexColor('#2d3748'),
            'section_line': colors.HexColor('#4299e1'),
            'accent': colors.HexColor('#63b3ed')
        },
        'compact': {
            'header_bg': colors.white,
            'header_text': colors.black,
            'section_line': colors.HexColor('#cbd5e0'),
            'accent': colors.HexColor('#4a5568')
        },
        'creative': {
            'header_bg': colors.HexColor('#1E1E1E'),
            'header_text': colors.HexColor('#F0E6D2'),
            'section_line': colors.HexColor('#D13639'),
            'accent': colors.HexColor('#C28F2C')
        }
    }
    
    return color_schemes.get(template, color_schemes['executive'])

