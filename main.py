import json
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether, Image
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def load_resume_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_resume(data):
    doc = SimpleDocTemplate("resume.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    # Custom fonts
    pdfmetrics.registerFont(TTFont('OpenSans-Regular', 'fonts/OpenSans-VariableFont_wdth,wght.ttf'))
    pdfmetrics.registerFont(TTFont('OpenSans-Italic', 'fonts/OpenSans-Italic-VariableFont_wdth,wght.ttf'))

    # Custom styles
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=22,
        spaceAfter=14,
        textColor=colors.darkblue
    )

    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=18,
        textColor=colors.darkblue,
        spaceBefore=12,
        spaceAfter=6
    )

    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=12,
        textColor=colors.black
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=12,
        textColor=colors.black,
        leftIndent=10,
        bulletFontName='Helvetica-Bold',
        bulletIndent=0
    )

    story = []

    # Header
    if 'name' in data and data['name'].strip():
        story.append(Paragraph(data['name'], title_style))
    if 'title' in data and data['title'].strip():
        story.append(Paragraph(data['title'], title_style))
    story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.darkblue, spaceBefore=6, spaceAfter=12))

    # Contact Information using a grid layout
    email_icon = 'icons/email.png'
    phone_icon = 'icons/phone.png'
    location_icon = 'icons/location.png'
    linkedin_icon = 'icons/linkedin.png'
    github_icon = 'icons/github.png'
    website_icon = 'icons/website.png'

    icon_size = 10

 

    contact_data = [
    [Image(email_icon, width=icon_size, height=icon_size), Paragraph(data['contact']['email'], normal_style),
     Spacer(1, 10),
     Image(phone_icon, width=icon_size, height=icon_size), Paragraph(data['contact']['phone'], normal_style),
     Spacer(1, 10),
     Image(location_icon, width=icon_size, height=icon_size), Paragraph(data['contact']['location'], normal_style)],
    
    [Image(linkedin_icon, width=icon_size, height=icon_size), Paragraph(f"<a href='{data['contact']['linkedin']}' color='blue'>{data['contact']['linkedin']}</a>", normal_style),
     Spacer(1, 10),
     Image(github_icon, width=icon_size, height=icon_size), Paragraph(f"<a href='{data['contact']['github']}' color='blue'>{data['contact']['github']}</a>", normal_style),
     Spacer(1, 10),
     Image(website_icon, width=icon_size, height=icon_size), Paragraph(f"<a href='{data['contact']['website']}' color='blue'>{data['contact']['website']}</a>", normal_style)]
]

    # Create a single-row table with multiple columns
    contact_table = Table(contact_data, hAlign='CENTER', colWidths=[icon_size, 2 * inch, 0.5 * inch, icon_size, 2 * inch, 0.5 * inch, icon_size, 2 * inch])
    contact_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'OpenSans-Regular'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))

    story.append(contact_table)
    story.append(Spacer(1, 20))

    # Summary
    if 'summary' in data and data['summary'].strip():
        story.append(Paragraph("Summary", subtitle_style))
        story.append(Paragraph(data['summary'], normal_style))
        story.append(Spacer(1, 12))

    # Technical Proficiency
    if 'technical_proficiency' in data:
        technical_proficiency_section = [Paragraph("Technical Proficiency", subtitle_style)]
        for key, value in data['technical_proficiency'].items():
            if value.strip():
                technical_proficiency_section.append(Paragraph(f"<b>{key.replace('_', ' ').title()}:</b> {value}", normal_style))
        if len(technical_proficiency_section) > 1:
            story.extend(technical_proficiency_section)
            story.append(Spacer(1, 12))

    # Experience
    if 'experience' in data:
        story.append(Paragraph("Experience", subtitle_style))
        for exp in data['experience']:
            exp_details = [
                Paragraph(f"<b>{exp['position']}</b> @ {exp['company']} ({exp['dates']})", normal_style)
            ]
            if 'responsibilities' in exp:
                for responsibility in exp['responsibilities']:
                    if responsibility.strip():
                        exp_details.append(Paragraph(f"• {responsibility}", bullet_style))
            story.extend(exp_details)
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 12))

    # Projects
    if 'projects' in data:
        project_section = [Paragraph("Projects", subtitle_style)]
        for project in data['projects']:
            if project['title'].strip():
                project_details = [
                    Paragraph(f"<b>{project['title']}</b> (<a href='{project['url']}' color='blue'>{project['url']}</a>)", normal_style),
                    Paragraph(project['description'], normal_style),
                    Paragraph(f"Technologies: {project['technologies']}", normal_style)
                ]
                project_section.extend(project_details)
                project_section.append(Spacer(1, 6))
        if len(project_section) > 1:
            story.extend(project_section)
            story.append(Spacer(1, 12))

    # Education
    if 'education' in data:
        education_section = [Paragraph("Education", subtitle_style)]
        for edu in data['education']:
            education_section.append(Paragraph(f"<b>{edu['degree']}</b>, {edu['institution']} ({edu['dates']})", normal_style))
            education_section.append(Spacer(1, 6))
        if len(education_section) > 1:
            story.extend(education_section)
            story.append(Spacer(1, 12))

    # Additional Experience
    if 'additional_experience' in data:
        additional_experience_section = [Paragraph("Additional Experience", subtitle_style)]
        for add_exp in data['additional_experience']:
            add_exp_details = [
                Paragraph(f"<b>{add_exp['position']}</b> @ {add_exp['company']} ({add_exp['dates']})", normal_style)
            ]
            if 'responsibilities' in add_exp:
                for responsibility in add_exp['responsibilities']:
                    if responsibility.strip():
                        add_exp_details.append(Paragraph(f"• {responsibility}", bullet_style))
            additional_experience_section.extend(add_exp_details)
            additional_experience_section.append(Spacer(1, 6))
        if len(additional_experience_section) > 1:
            story.extend(additional_experience_section)
            story.append(Spacer(1, 12))

    # Skills
    if 'skills' in data and data['skills']:
        skills_section = [Paragraph("Skills", subtitle_style)]
        skill_items = [Paragraph(f"• {skill}", bullet_style) for skill in data['skills'] if skill.strip()]
        if skill_items:
            skills_table = Table([skill_items[i:i+3] for i in range(0, len(skill_items), 3)], hAlign='LEFT')
            skills_section.append(skills_table)
            story.extend(skills_section)

    # Build the PDF
    doc.build(story)

if __name__ == "__main__":
    resume_data = load_resume_data("resume_data.json")
    generate_resume(resume_data)
