"""
Two-column resume layout with sidebar.
Optimized for technical roles - skills sidebar + main content.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Frame, PageTemplate, BaseDocTemplate
)
from reportlab.lib import colors as rl_colors

from layouts.base_layout import (
    LayoutConfig,
    ResumeSection,
    create_compact_header,
    format_experience_entry,
    format_skills_inline,
    format_technical_proficiency_compact
)


class TwoColumnDocTemplate(BaseDocTemplate):
    """Custom document template for two-column layout."""
    
    def __init__(self, filename, **kwargs):
        BaseDocTemplate.__init__(self, filename, **kwargs)
        
        # Page dimensions
        page_width, page_height = letter
        
        # Margins
        left_margin = kwargs.get('leftMargin', 0.5 * inch)
        right_margin = kwargs.get('rightMargin', 0.5 * inch)
        top_margin = kwargs.get('topMargin', 0.5 * inch)
        bottom_margin = kwargs.get('bottomMargin', 0.5 * inch)
        
        # Calculate usable width
        usable_width = page_width - left_margin - right_margin
        
        # Sidebar width (30% of usable width)
        sidebar_width = usable_width * 0.30
        main_width = usable_width * 0.68  # 2% gap
        
        # Define frames
        # Left sidebar frame
        sidebar_frame = Frame(
            left_margin,
            bottom_margin,
            sidebar_width,
            page_height - top_margin - bottom_margin,
            id='sidebar',
            showBoundary=0
        )
        
        # Right main content frame
        main_frame = Frame(
            left_margin + sidebar_width + (usable_width * 0.02),  # Add 2% gap
            bottom_margin,
            main_width,
            page_height - top_margin - bottom_margin,
            id='main',
            showBoundary=0
        )
        
        # Create page template with two frames
        template = PageTemplate(
            id='TwoColumn',
            frames=[sidebar_frame, main_frame]
        )
        
        self.addPageTemplates([template])


def generate_two_column_resume(data, styles, template='technical', density='compact', output_file='resume.pdf'):
    """
    Generate a two-column resume with sidebar.
    
    Args:
        data: Resume data dictionary
        styles: Style dictionary from professional_styles
        template: Template name for color scheme
        density: Layout density
        output_file: Output PDF filename
    """
    # Create layout configuration
    config = LayoutConfig(density=density)
    
    # Create two-column document
    doc = TwoColumnDocTemplate(
        output_file,
        pagesize=letter,
        topMargin=config.margins['top'],
        bottomMargin=config.margins['bottom'],
        leftMargin=config.margins['left'],
        rightMargin=config.margins['right']
    )
    
    story = []
    
    # SIDEBAR CONTENT (Frame 1)
    # Name and title at top of sidebar
    name = data.get('name', '')
    if name:
        story.append(Paragraph(name, styles['Name']))
        story.append(Spacer(1, 3))
    
    title = data.get('title', '')
    if title:
        story.append(Paragraph(title, styles['Title']))
        story.append(config.get_spacer('section'))
    
    # Contact info in sidebar
    contact = data.get('contact', {})
    if contact:
        story.append(Paragraph('<b>CONTACT</b>', styles['SectionHeader']))
        story.append(config.get_spacer('line'))
        
        if contact.get('email'):
            story.append(Paragraph(f'<font size="8">{contact["email"]}</font>', styles['Contact']))
            story.append(Spacer(1, 2))
        if contact.get('phone'):
            story.append(Paragraph(f'<font size="8">{contact["phone"]}</font>', styles['Contact']))
            story.append(Spacer(1, 2))
        if contact.get('location'):
            story.append(Paragraph(f'<font size="8">{contact["location"]}</font>', styles['Contact']))
            story.append(Spacer(1, 2))
        if contact.get('linkedin'):
            linkedin_short = contact['linkedin'].replace('https://', '').replace('http://', '').replace('linkedin.com/in/', '')
            story.append(Paragraph(f'<font size="7"><a href="{contact["linkedin"]}" color="{styles["_colors"]["link"]}">{linkedin_short}</a></font>', styles['Contact']))
            story.append(Spacer(1, 2))
        if contact.get('github'):
            github_short = contact['github'].replace('https://', '').replace('http://', '').replace('github.com/', '')
            story.append(Paragraph(f'<font size="7"><a href="{contact["github"]}" color="{styles["_colors"]["link"]}">{github_short}</a></font>', styles['Contact']))
            story.append(Spacer(1, 2))
        if contact.get('website'):
            website_short = contact['website'].replace('https://', '').replace('http://', '')
            story.append(Paragraph(f'<font size="7"><a href="{contact["website"]}" color="{styles["_colors"]["link"]}">{website_short}</a></font>', styles['Contact']))
        
        story.append(config.get_spacer('section'))
    
    # Skills in sidebar (if available)
    skills = data.get('skills', [])
    if skills:
        story.append(Paragraph('<b>SKILLS</b>', styles['SectionHeader']))
        story.append(config.get_spacer('line'))
        
        if isinstance(skills, str):
            skills = [s.strip() for s in skills.split(',')]
        
        for skill in skills:
            if skill.strip():
                story.append(Paragraph(f'<font size="8">• {skill.strip()}</font>', styles['SkillsText']))
                story.append(Spacer(1, 1))
        
        story.append(config.get_spacer('section'))
    
    # Technical Proficiency in sidebar (compact)
    tech_prof = data.get('technical_proficiency', {})
    if tech_prof:
        story.append(Paragraph('<b>TECHNICAL</b>', styles['SectionHeader']))
        story.append(config.get_spacer('line'))
        
        for key, value in tech_prof.items():
            formatted_key = key.replace('_', ' ').title()
            # Very compact format for sidebar
            story.append(Paragraph(f'<font size="7"><b>{formatted_key}:</b></font>', styles['TechProfText']))
            story.append(Paragraph(f'<font size="7">{value}</font>', styles['TechProfText']))
            story.append(Spacer(1, 3))
        
        story.append(config.get_spacer('section'))
    
    # Education in sidebar
    education = data.get('education', [])
    if education:
        story.append(Paragraph('<b>EDUCATION</b>', styles['SectionHeader']))
        story.append(config.get_spacer('line'))
        
        for edu in education:
            degree = edu.get('degree', '')
            institution = edu.get('institution', '')
            dates = edu.get('dates', '')
            
            if degree:
                story.append(Paragraph(f'<font size="8"><b>{degree}</b></font>', styles['EducationText']))
                story.append(Spacer(1, 1))
            if institution:
                story.append(Paragraph(f'<font size="8">{institution}</font>', styles['EducationText']))
                story.append(Spacer(1, 1))
            if dates:
                story.append(Paragraph(f'<font size="7"><i>{dates}</i></font>', styles['EducationText']))
            
            story.append(Spacer(1, 4))
    
    # Frame break - move to main content area
    story.append(PageBreak())
    
    # MAIN CONTENT (Frame 2)
    # Professional Summary
    summary = data.get('summary', '')
    if summary:
        story.append(Paragraph('<b>PROFESSIONAL SUMMARY</b>', styles['SectionHeader']))
        section = ResumeSection(styles, config)
        section.add_separator_line(color=styles['_colors']['primary'], width=1.2 * inch)
        story.extend(section.get_story())
        
        if isinstance(summary, list):
            summary = ' '.join(summary)
        
        story.append(Paragraph(summary, styles['BodyText']))
        story.append(config.get_spacer('section'))
    
    # Professional Experience
    experience = data.get('experience', [])
    if experience:
        story.append(Paragraph('<b>PROFESSIONAL EXPERIENCE</b>', styles['SectionHeader']))
        section = ResumeSection(styles, config)
        section.add_separator_line(color=styles['_colors']['primary'], width=1.2 * inch)
        story.extend(section.get_story())
        
        for i, exp in enumerate(experience):
            story.extend(format_experience_entry(exp, styles, config))
    
    # Projects
    projects = data.get('projects', [])
    if projects:
        story.append(Paragraph('<b>PROJECTS</b>', styles['SectionHeader']))
        section = ResumeSection(styles, config)
        section.add_separator_line(color=styles['_colors']['primary'], width=1.2 * inch)
        story.extend(section.get_story())
        
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
                story.append(config.get_spacer('line'))
            
            if description:
                story.append(Paragraph(description, styles['ProjectDesc']))
                story.append(config.get_spacer('line'))
            
            if technologies:
                story.append(Paragraph(f'<i>Tech: {technologies}</i>', styles['TechText']))
                story.append(config.get_spacer('subsection'))
    
    # Build the PDF
    doc.build(story)
    
    return output_file

