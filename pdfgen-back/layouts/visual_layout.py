"""
Visual layout generator - generates PDF from user-defined section layout.
Gives users complete control over what appears, order, and dimensions.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
)
from reportlab.lib import colors as rl_colors

from styles.professional_styles import get_professional_styles
from layouts.base_layout import (
    LayoutConfig,
    create_compact_header,
    format_experience_entry,
    format_skills_inline,
    format_technical_proficiency_compact
)


def parse_dimension(value, default='auto'):
    """Parse dimension value (100%, 50px, auto, etc.)"""
    if value == 'auto':
        return None
    if value.endswith('px'):
        return float(value.replace('px', ''))
    if value.endswith('%'):
        # Return as decimal (e.g., '100%' -> 1.0)
        return float(value.replace('%', '')) / 100.0
    return default


def generate_visual_layout(data, layout_config, output_file='resume.pdf'):
    """
    Generate PDF from visual layout configuration.
    
    Args:
        data: Resume data dictionary (full resume data, fallback)
        layout_config: Layout configuration from frontend
        output_file: Output PDF filename
    """
    # Get template and styles
    template = layout_config.get('template', 'executive')
    styles = get_professional_styles(template=template, density='balanced')
    config = LayoutConfig(density='balanced')
    
    # Create document
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        topMargin=config.margins['top'],
        bottomMargin=config.margins['bottom'],
        leftMargin=config.margins['left'],
        rightMargin=config.margins['right']
    )
    
    story = []
    sections = layout_config.get('sections', [])
    
    # Debug: Print sections to verify order
    print(f"\n=== VISUAL LAYOUT: Processing {len(sections)} sections ===")
    for i, s in enumerate(sections):
        has_data = s.get('data') is not None and bool(s.get('data'))
        print(f"  {i+1}. {s.get('type')} (has_data: {has_data})")
    print("=" * 60)
    
    # Process each section IN THE ORDER PROVIDED
    for idx, section in enumerate(sections):
        section_type = section.get('type')
        section_data = section.get('data', {})
        padding_type = section.get('padding', 'medium')
        
        # Debug each section
        print(f"[{idx+1}] Processing: {section_type}, data keys: {list(section_data.keys()) if section_data else 'None'}")
        
        # Add spacing based on padding
        padding_map = {
            'none': 0,
            'small': 4,
            'medium': 8,
            'large': 12
        }
        padding = padding_map.get(padding_type, 8)
        
        # Generate content based on section type
        if section_type == 'header':
            elements = create_header_section(section_data, styles, config)
            story.extend(elements)
            
        elif section_type == 'summary':
            summary = section_data.get('summary', '')
            if summary:
                story.append(Paragraph('<b>PROFESSIONAL SUMMARY</b>', styles['SectionHeader']))
                story.append(Spacer(1, 4))
                if isinstance(summary, list):
                    summary = ' '.join(summary)
                story.append(Paragraph(summary, styles['BodyText']))
                
        elif section_type == 'experience':
            experiences = section_data.get('experience', [])
            if experiences:
                story.append(Paragraph('<b>PROFESSIONAL EXPERIENCE</b>', styles['SectionHeader']))
                story.append(Spacer(1, 4))
                for exp in experiences:
                    story.extend(format_experience_entry(exp, styles, config))
                    
        elif section_type == 'education':
            education = section_data.get('education', [])
            if education:
                story.append(Paragraph('<b>EDUCATION</b>', styles['SectionHeader']))
                story.append(Spacer(1, 4))
                for edu in education:
                    degree = edu.get('degree', '')
                    institution = edu.get('institution', '')
                    dates = edu.get('dates', '')
                    
                    if degree or institution:
                        edu_text = ''
                        if degree:
                            edu_text = f'<b>{degree}</b>'
                        if institution:
                            edu_text += f' | {institution}' if edu_text else institution
                        if dates:
                            edu_text += f' | {dates}'
                        
                        story.append(Paragraph(edu_text, styles['EducationText']))
                        story.append(Spacer(1, 3))
                        
        elif section_type == 'skills':
            skills = section_data.get('skills', [])
            if skills:
                story.append(Paragraph('<b>SKILLS</b>', styles['SectionHeader']))
                story.append(Spacer(1, 4))
                story.append(format_skills_inline(skills, styles))
                
        elif section_type == 'projects':
            projects = section_data.get('projects', [])
            if projects:
                story.append(Paragraph('<b>PROJECTS</b>', styles['SectionHeader']))
                story.append(Spacer(1, 4))
                for project in projects:
                    title = project.get('title', '')
                    url = project.get('url', '')
                    description = project.get('description', '')
                    technologies = project.get('technologies', '')
                    
                    if title:
                        if url:
                            url_display = url.replace('https://', '').replace('http://', '')[:35]
                            title_text = f'<b>{title}</b> (<a href="{url}" color="{styles["_colors"]["link"]}">{url_display}</a>)'
                        else:
                            title_text = f'<b>{title}</b>'
                        
                        story.append(Paragraph(title_text, styles['ProjectTitle']))
                        story.append(Spacer(1, 2))
                        
                        if description:
                            story.append(Paragraph(description, styles['ProjectDesc']))
                            story.append(Spacer(1, 2))
                        
                        if technologies:
                            story.append(Paragraph(f'<i>Technologies: {technologies}</i>', styles['TechText']))
                            story.append(Spacer(1, 4))
                            
        elif section_type == 'technical_proficiency':
            tech_prof = section_data.get('technical_proficiency', {})
            if tech_prof:
                story.append(Paragraph('<b>TECHNICAL PROFICIENCY</b>', styles['SectionHeader']))
                story.append(Spacer(1, 4))
                story.extend(format_technical_proficiency_compact(tech_prof, styles, config))
                
        elif section_type == 'spacer':
            # Add empty space with specified height
            height = section.get('height', '20px')
            height_value = parse_dimension(height, 20)
            if height_value:
                story.append(Spacer(1, height_value))
                
        elif section_type == 'divider':
            # Add horizontal line
            color = section.get('color', '#cccccc')
            thickness = section.get('thickness', '1px')
            
            # Create divider line
            line_table = Table([['']], colWidths=[7.0 * inch], rowHeights=[0.5])
            line_table.setStyle(TableStyle([
                ('LINEABOVE', (0, 0), (-1, 0), float(thickness.replace('px', '')), 
                 rl_colors.HexColor(color)),
            ]))
            story.append(line_table)
        
        # Add section padding
        if padding > 0:
            story.append(Spacer(1, padding))
    
    # Build PDF
    doc.build(story)
    return output_file


def create_header_section(data, styles, config):
    """Create header section with name, title, contact."""
    story = []
    
    name = data.get('name', '')
    if name:
        story.append(Paragraph(name, styles['Name']))
        story.append(Spacer(1, 2))
    
    title = data.get('title', '')
    if title:
        story.append(Paragraph(title, styles['Title']))
        story.append(Spacer(1, 4))
    
    # Contact info inline
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
        story.append(Spacer(1, 8))
    
    return story

