"""
Base layout utilities and shared functions for all resume layouts.
"""
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib import colors as rl_colors


class LayoutConfig:
    """Configuration for layout spacing and dimensions."""
    
    def __init__(self, density='balanced'):
        """
        Initialize layout configuration.
        
        Args:
            density: 'compact', 'balanced', or 'spacious'
        """
        self.density = density
        
        # Margin configurations based on density
        margins = {
            'compact': {
                'top': 0.4 * inch,
                'bottom': 0.4 * inch,
                'left': 0.5 * inch,
                'right': 0.5 * inch
            },
            'balanced': {
                'top': 0.5 * inch,
                'bottom': 0.5 * inch,
                'left': 0.6 * inch,
                'right': 0.6 * inch
            },
            'spacious': {
                'top': 0.75 * inch,
                'bottom': 0.75 * inch,
                'left': 0.75 * inch,
                'right': 0.75 * inch
            }
        }
        
        # Spacing configurations
        spacing = {
            'compact': {
                'section': 8,
                'subsection': 4,
                'item': 2,
                'line': 1
            },
            'balanced': {
                'section': 10,
                'subsection': 5,
                'item': 3,
                'line': 2
            },
            'spacious': {
                'section': 14,
                'subsection': 8,
                'item': 5,
                'line': 3
            }
        }
        
        self.margins = margins.get(density, margins['balanced'])
        self.spacing = spacing.get(density, spacing['balanced'])
    
    def get_spacer(self, space_type='section'):
        """Get a Spacer object for the specified type."""
        height = self.spacing.get(space_type, self.spacing['section'])
        return Spacer(1, height)


class ResumeSection:
    """Base class for resume sections with consistent styling."""
    
    def __init__(self, styles, config):
        """
        Initialize section builder.
        
        Args:
            styles: Dictionary of ParagraphStyle objects
            config: LayoutConfig instance
        """
        self.styles = styles
        self.config = config
        self.story = []
    
    def add_section_header(self, title, style_name='SectionHeader'):
        """Add a styled section header."""
        self.story.append(self.config.get_spacer('section'))
        self.story.append(Paragraph(title, self.styles[style_name]))
        self.story.append(self.config.get_spacer('subsection'))
    
    def add_item(self, text, style_name='BodyText'):
        """Add a simple text item."""
        self.story.append(Paragraph(text, self.styles[style_name]))
        self.story.append(self.config.get_spacer('item'))
    
    def add_bullet_item(self, text, style_name='BulletText'):
        """Add a bullet point item."""
        bullet_text = f"• {text}"
        self.story.append(Paragraph(bullet_text, self.styles[style_name]))
        self.story.append(self.config.get_spacer('line'))
    
    def add_separator_line(self, color=rl_colors.HexColor('#CCCCCC'), width=None):
        """Add a horizontal separator line."""
        from reportlab.platypus import Table, TableStyle
        
        if width is None:
            width = 7.5 * inch  # Default page width minus margins
        
        line_table = Table([['']], colWidths=[width], rowHeights=[0.5])
        line_table.setStyle(TableStyle([
            ('LINEABOVE', (0, 0), (-1, 0), 0.5, color),
        ]))
        self.story.append(line_table)
        self.story.append(self.config.get_spacer('line'))
    
    def get_story(self):
        """Return the accumulated story elements."""
        return self.story


def create_compact_header(data, styles, config):
    """
    Create a compact, space-efficient header.
    
    Args:
        data: Resume data dictionary
        styles: Style dictionary
        config: LayoutConfig instance
    
    Returns:
        List of flowable elements
    """
    story = []
    
    # Name - large and bold
    name = data.get('name', '')
    if name:
        story.append(Paragraph(name, styles['Name']))
        story.append(Spacer(1, 2))
    
    # Title/Role - directly under name
    title = data.get('title', '')
    if title:
        story.append(Paragraph(title, styles['Title']))
        story.append(config.get_spacer('subsection'))
    
    # Contact info - single line, inline
    contact = data.get('contact', {})
    contact_parts = []
    
    if contact.get('email'):
        contact_parts.append(contact['email'])
    if contact.get('phone'):
        contact_parts.append(contact['phone'])
    if contact.get('location'):
        contact_parts.append(contact['location'])
    if contact.get('linkedin'):
        linkedin_display = contact['linkedin'].replace('https://', '').replace('http://', '')
        contact_parts.append(f'<a href="{contact["linkedin"]}">{linkedin_display}</a>')
    if contact.get('github'):
        github_display = contact['github'].replace('https://', '').replace('http://', '')
        contact_parts.append(f'<a href="{contact["github"]}">{github_display}</a>')
    if contact.get('website'):
        website_display = contact['website'].replace('https://', '').replace('http://', '')
        contact_parts.append(f'<a href="{contact["website"]}">{website_display}</a>')
    
    if contact_parts:
        contact_line = ' | '.join(contact_parts)
        story.append(Paragraph(contact_line, styles['Contact']))
        story.append(config.get_spacer('section'))
    
    return story


def format_experience_entry(exp, styles, config):
    """
    Format a single experience entry with bold, prominent formatting.
    
    Args:
        exp: Experience dictionary
        styles: Style dictionary
        config: LayoutConfig instance
    
    Returns:
        List of flowable elements
    """
    story = []
    
    # Job title, company, and dates on one line
    position = exp.get('position', '')
    company = exp.get('company', '')
    dates = exp.get('dates', '')
    location = exp.get('location', '')
    
    # Only add if we have at least position or company
    if not position and not company:
        return story
    
    # Format with BOLD position and company, dates aligned right
    header_parts = []
    if position:
        header_parts.append(f"<b>{position}</b>")
    if company:
        header_parts.append(f"<b>{company}</b>")
    if location:
        header_parts.append(location)
    
    header_text = " | ".join(header_parts)
    
    # Add dates on same line if present
    if dates:
        header_text += f" <b>({dates})</b>"
    
    story.append(Paragraph(header_text, styles['JobHeader']))
    story.append(config.get_spacer('line'))
    
    # Responsibilities as bullets
    responsibilities = exp.get('responsibilities', [])
    if isinstance(responsibilities, str):
        responsibilities = [responsibilities]
    
    for responsibility in responsibilities:
        if responsibility.strip():
            story.append(Paragraph(f"• {responsibility.strip()}", styles['BulletText']))
            story.append(config.get_spacer('line'))
    
    # Technologies if present
    technologies = exp.get('technologies', '')
    if technologies:
        story.append(Paragraph(f"<i>Technologies: {technologies}</i>", styles['TechText']))
    
    story.append(config.get_spacer('subsection'))
    
    return story


def format_skills_inline(skills, styles):
    """
    Format skills as inline tags/comma-separated list.
    
    Args:
        skills: List of skills or string
        styles: Style dictionary
    
    Returns:
        Paragraph object
    """
    if isinstance(skills, str):
        skills = [s.strip() for s in skills.split(',')]
    elif isinstance(skills, list):
        skills = [str(s).strip() for s in skills]
    else:
        skills = []
    
    # Join with bullet separator for clean look
    skills_text = ' • '.join(skills)
    return Paragraph(skills_text, styles['SkillsText'])


def format_technical_proficiency_compact(tech_prof, styles, config):
    """
    Format technical proficiency in a compact, readable way.
    
    Args:
        tech_prof: Dictionary of technical proficiency categories
        styles: Style dictionary
        config: LayoutConfig instance
    
    Returns:
        List of flowable elements
    """
    story = []
    
    for key, value in tech_prof.items():
        if value:
            formatted_key = key.replace('_', ' ').title()
            # Put category name in bold, followed by skills
            text = f"<b>{formatted_key}:</b> {value}"
            story.append(Paragraph(text, styles['TechProfText']))
            story.append(config.get_spacer('line'))
    
    return story

