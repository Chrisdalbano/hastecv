import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
from reportlab.lib import colors
from reportlab.platypus.flowables import KeepTogether
from styles import get_styles

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def generate_resume(data, template="default"):
    doc = SimpleDocTemplate("resume.pdf", pagesize=letter)
    styles = get_styles(template=template)

    story = []

    # Define header background colors based on the template
    header_bg_colors = {
        'default': '#262626',
        'modern': '#333333',
        'minimal': '#FFFFFF'  # No header background
    }

    header_bg_color = header_bg_colors.get(template)

    # Define the header height
    header_height = 1 * inch

    # Function to draw the header background
    def draw_header_background(canvas, doc):
        if header_bg_color and header_bg_color != '#FFFFFF':
            canvas.saveState()
            canvas.setFillColorRGB(*hex_to_rgb(header_bg_color))
            canvas.rect(0, doc.height + doc.topMargin - header_height, doc.width, header_height, fill=1)
            canvas.restoreState()

    # Header content
    header_content = []

    if 'name' in data and data['name'].strip():
        header_content.append(Paragraph(data['name'], styles['CustomTitle']))
    if 'title' in data and data['title'].strip():
        header_content.append(Paragraph(data['title'], styles['CustomH2']))
    header_content.append(HRFlowable(width="100%", thickness=2, lineCap='round', color=colors.white, spaceBefore=6, spaceAfter=12))

    # Wrap header content in KeepTogether and add to story
    story.append(KeepTogether(header_content))

    # Contact Information using a centered 2x3 grid layout
    icons_path = os.path.join(os.path.dirname(__file__), 'static', 'icons')
    email_icon = os.path.join(icons_path, 'email.png')
    phone_icon = os.path.join(icons_path, 'phone.png')
    location_icon = os.path.join(icons_path, 'location.png')
    linkedin_icon = os.path.join(icons_path, 'linkedin.png')
    github_icon = os.path.join(icons_path, 'github.png')
    website_icon = os.path.join(icons_path, 'website.png')

    icon_size = 11
    icon_text_gap = 6  # Adjust the gap as needed

    def generate_contact_row(icon_path, text, link=None):
        if text:
            if link:
                text = f"<a href='{link}' color='darkorange'>{link.replace('https://', '')}</a>"
            return [Image(icon_path, width=icon_size, height=icon_size), Spacer(icon_text_gap, 0), Paragraph(text, styles['CustomNormal'])]
        return None

    contact_data = []
    contact_info = data.get('contact', {})

    contact_data.append(generate_contact_row(email_icon, contact_info.get('email')))
    contact_data.append(generate_contact_row(linkedin_icon, contact_info.get('linkedin'), contact_info.get('linkedin')))
    contact_data.append(generate_contact_row(location_icon, contact_info.get('location')))
    contact_data.append(generate_contact_row(github_icon, contact_info.get('github'), contact_info.get('github')))
    contact_data.append(generate_contact_row(phone_icon, contact_info.get('phone')))
    contact_data.append(generate_contact_row(website_icon, contact_info.get('website'), contact_info.get('website')))

    # Filter out None values from contact_data
    contact_data = [row for row in contact_data if row is not None]

    # Arrange the contact data in a 2x3 grid
    contact_grid_data = []

    # Ensure we have pairs to create rows correctly
    for i in range(0, len(contact_data), 2):
        if i + 1 < len(contact_data):
            contact_grid_data.append(contact_data[i] + contact_data[i + 1])
        else:
            # Handle the case where there's an odd number of items
            contact_grid_data.append(contact_data[i])

    contact_table = Table(contact_grid_data, hAlign='CENTER', colWidths=[icon_size, icon_text_gap, 2.4 * inch, icon_size, icon_text_gap, 2.4 * inch])
    contact_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'OpenSans-Regular'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))

    story.append(contact_table)
    story.append(Spacer(1, 20))

    # Summary
    if 'summary' in data and isinstance(data['summary'], list):
        story.append(Paragraph("Summary", styles['CustomSubtitle']))
        
        for summary_line in data['summary']:
            if summary_line.strip():  # Ensure non-empty lines are processed
                story.append(Paragraph(summary_line, styles['CustomNormal']))
        
        story.append(Spacer(1, 12))

    # Technical Proficiency
    if 'technical_proficiency' in data:
        technical_proficiency_section = [Paragraph("Technical Proficiency", styles['CustomSubtitle'])]
        for key, value in data['technical_proficiency'].items():
            if value.strip():
                technical_proficiency_section.append(Paragraph(f"<b>{key.replace('_', ' ').title()}:</b> {value}", styles['CustomNormal']))
        if len(technical_proficiency_section) > 1:
            story.extend(technical_proficiency_section)
            story.append(Spacer(1, 12))

    # Experience
    if 'experience' in data:
        story.append(Paragraph("Experience", styles['CustomSubtitle']))
        for exp in data['experience']:
            exp_details = [
                Paragraph(f"<b>{exp['position']}</b> @ {exp['company']} ({exp['dates']})", styles['CustomBold'])
            ]
            if 'responsibilities' in exp:
                for responsibility in exp['responsibilities']:
                    if responsibility.strip():
                        exp_details.append(Paragraph(f"• {responsibility}", styles['CustomBullet']))
            story.extend(exp_details)
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 12))

    # Projects
    if 'projects' in data:
        project_section = [Paragraph("Projects", styles['CustomSubtitle'])]
        for project in data['projects']:
            if project['title'].strip():
                project_details = [
                    Paragraph(f"<b>{project['title']}</b> (<a href='{project['url']}' color='darkorange'>{project['url']}</a>)", styles['CustomBold']),
                    Paragraph(project['description'], styles['CustomNormal']),
                    Paragraph(f"Technologies: {project['technologies']}", styles['CustomNormal'])
                ]
                project_section.extend(project_details)
                project_section.append(Spacer(1, 6))
        if len(project_section) > 1:
            story.extend(project_section)
            story.append(Spacer(1, 12))

    # Education
    if 'education' in data:
        education_section = [Paragraph("Education", styles['CustomSubtitle'])]
        for edu in data['education']:
            education_section.append(Paragraph(f"<b>{edu['degree']}</b>, {edu['institution']} ({edu['dates']})", styles['CustomNormal']))
            education_section.append(Spacer(1, 6))
        if len(education_section) > 1:
            story.extend(education_section)
            story.append(Spacer(1, 12))

    # Additional Experience
    if 'additional_experience' in data:
        additional_experience_section = [Paragraph("Additional Experience", styles['CustomSubtitle'])]
        for add_exp in data['additional_experience']:
            add_exp_details = [
                Paragraph(f"<b>{add_exp['position']}</b> @ {add_exp['company']} ({add_exp['dates']})", styles['CustomBold'])
            ]
            if 'responsibilities' in add_exp:
                for responsibility in add_exp['responsibilities']:
                    if responsibility.strip():
                        add_exp_details.append(Paragraph(f"• {responsibility}", styles['CustomBullet']))
            additional_experience_section.extend(add_exp_details)
            additional_experience_section.append(Spacer(1, 6))
        if len(additional_experience_section) > 1:
            story.extend(additional_experience_section)
            story.append(Spacer(1, 12))

    # Skills
    if 'skills' in data and data['skills']:
        skills_section = [Paragraph("Skills", styles['CustomSubtitle'])]
        skill_items = [Paragraph(f"• {skill}", styles['CustomBullet']) for skill in data['skills'] if skill.strip()]
        if skill_items:
            skills_table = Table([skill_items[i:i+3] for i in range(0, len(skill_items), 3)], hAlign='LEFT')
            skills_section.append(skills_table)
            story.extend(skills_section)

    # Build the PDF
    doc.build(story, onFirstPage=draw_header_background if header_bg_color else None)
