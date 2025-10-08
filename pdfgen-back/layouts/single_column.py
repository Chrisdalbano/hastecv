"""
Single-column professional resume layout.
Optimized for traditional/corporate roles.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib import colors as rl_colors

from layouts.base_layout import (
    LayoutConfig,
    ResumeSection,
    create_compact_header,
    format_experience_entry,
    format_skills_inline,
    format_technical_proficiency_compact
)


def generate_single_column_resume(data, styles, template='executive', density='balanced', output_file='resume.pdf'):
    """
    Generate a professional single-column resume.
    
    Args:
        data: Resume data dictionary
        styles: Style dictionary from professional_styles
        template: Template name for color scheme
        density: Layout density ('compact', 'balanced', 'spacious')
        output_file: Output PDF filename
    """
    # Create layout configuration
    config = LayoutConfig(density=density)
    
    # Create document with optimized margins
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        topMargin=config.margins['top'],
        bottomMargin=config.margins['bottom'],
        leftMargin=config.margins['left'],
        rightMargin=config.margins['right']
    )
    
    story = []
    
    # Add header (name, title, contact)
    header_elements = create_compact_header(data, styles, config)
    if header_elements:
        story.extend(header_elements)
        
        # Add spacing after header
        story.append(config.get_spacer('section'))
    
    # Professional Summary
    summary = data.get('summary', '')
    if summary:
        story.append(Paragraph('<b>PROFESSIONAL SUMMARY</b>', styles['SectionHeader']))
        story.append(config.get_spacer('subsection'))
        
        if isinstance(summary, list):
            summary = ' '.join(summary)
        
        story.append(Paragraph(summary, styles['BodyText']))
        story.append(config.get_spacer('section'))
    
    # Technical Proficiency / Skills (compact format)
    tech_prof = data.get('technical_proficiency', {})
    if tech_prof and any(tech_prof.values()):  # Only show if has content
        story.append(Paragraph('<b>TECHNICAL PROFICIENCY</b>', styles['SectionHeader']))
        story.append(config.get_spacer('subsection'))
        
        story.extend(format_technical_proficiency_compact(tech_prof, styles, config))
        story.append(config.get_spacer('section'))
    
    # Professional Experience
    experience = data.get('experience', [])
    if experience and len(experience) > 0:
        story.append(Paragraph('<b>PROFESSIONAL EXPERIENCE</b>', styles['SectionHeader']))
        story.append(config.get_spacer('subsection'))
        
        for i, exp in enumerate(experience):
            exp_elements = format_experience_entry(exp, styles, config)
            if exp_elements:  # Only add if has content
                story.extend(exp_elements)
        
        story.append(config.get_spacer('section'))
    
    # Projects
    projects = data.get('projects', [])
    if projects and len(projects) > 0:
        story.append(Paragraph('<b>PROJECTS</b>', styles['SectionHeader']))
        story.append(config.get_spacer('subsection'))
        
        for project in projects:
            title = project.get('title', '')
            url = project.get('url', '')
            description = project.get('description', '')
            technologies = project.get('technologies', '')
            
            # Only add project if it has at least a title
            if not title:
                continue
            
            # Project title with link
            if url:
                # Clean up URL for display
                url_display = url.replace('https://', '').replace('http://', '')
                if len(url_display) > 40:
                    url_display = url_display[:40] + '...'
                title_text = f'<b>{title}</b> (<a href="{url}" color="{styles["_colors"]["link"]}">{url_display}</a>)'
            else:
                title_text = f'<b>{title}</b>'
            
            story.append(Paragraph(title_text, styles['ProjectTitle']))
            story.append(config.get_spacer('line'))
            
            # Description
            if description:
                story.append(Paragraph(description, styles['ProjectDesc']))
                story.append(config.get_spacer('line'))
            
            # Technologies
            if technologies:
                story.append(Paragraph(f'<i>Technologies: {technologies}</i>', styles['TechText']))
                story.append(config.get_spacer('subsection'))
        
        story.append(config.get_spacer('section'))
    
    # Education
    education = data.get('education', [])
    if education and len(education) > 0:
        story.append(Paragraph('<b>EDUCATION</b>', styles['SectionHeader']))
        story.append(config.get_spacer('subsection'))
        
        for edu in education:
            degree = edu.get('degree', '')
            institution = edu.get('institution', '')
            dates = edu.get('dates', '')
            
            # Only show if has at least degree or institution
            if degree or institution:
                edu_text = ''
                if degree:
                    edu_text = f'<b>{degree}</b>'
                if institution:
                    edu_text += f' | {institution}' if edu_text else institution
                if dates:
                    edu_text += f' | {dates}'
                
                story.append(Paragraph(edu_text, styles['EducationText']))
                story.append(config.get_spacer('line'))
        
        story.append(config.get_spacer('section'))
    
    # Skills (if not already included in technical proficiency)
    skills = data.get('skills', [])
    if skills and len(skills) > 0 and not tech_prof:
        story.append(Paragraph('<b>SKILLS</b>', styles['SectionHeader']))
        story.append(config.get_spacer('subsection'))
        
        story.append(format_skills_inline(skills, styles))
        story.append(config.get_spacer('section'))
    
    # Additional Experience (if present)
    additional_exp = data.get('additional_experience', [])
    if additional_exp and len(additional_exp) > 0:
        story.append(Paragraph('<b>ADDITIONAL EXPERIENCE</b>', styles['SectionHeader']))
        story.append(config.get_spacer('subsection'))
        
        for exp in additional_exp:
            exp_elements = format_experience_entry(exp, styles, config)
            if exp_elements:
                story.extend(exp_elements)
    
    # Build the PDF
    doc.build(story)
    
    return output_file

