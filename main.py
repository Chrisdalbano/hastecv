import json
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether, PageBreak, Image
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def load_resume_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_resume(data):
    doc = SimpleDocTemplate("resume.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    # custom fonts
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
    story.append(Paragraph(data['name'], title_style))
    story.append(Paragraph(data['title'], title_style))
    story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.darkblue, spaceBefore=6, spaceAfter=12))

    # Contact Information using a grid layout
    contact_data = [
        [Paragraph('<b>Email:</b>', normal_style), Paragraph(data['contact']['email'], normal_style)],
        [Paragraph('<b>Phone:</b>', normal_style), Paragraph(data['contact']['phone'], normal_style)],
        [Paragraph('<b>Location:</b>', normal_style), Paragraph(data['contact']['location'], normal_style)],
        [Paragraph('<b>LinkedIn:</b>', normal_style), Paragraph(f"<a href='{data['contact']['linkedin']}' color='blue'>{data['contact']['linkedin']}</a>", normal_style)],
        [Paragraph('<b>GitHub:</b>', normal_style), Paragraph(f"<a href='{data['contact']['github']}' color='blue'>{data['contact']['github']}</a>", normal_style)],
        [Paragraph('<b>Website:</b>', normal_style), Paragraph(f"<a href='{data['contact']['website']}' color='blue'>{data['contact']['website']}</a>", normal_style)]
    ]

    contact_table = Table(contact_data, hAlign='LEFT', colWidths=[1.5 * inch, 2.5 * inch, 1.5 * inch, 2.5 * inch])
    contact_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT')
    ]))
    story.append(contact_table)
    story.append(Spacer(1, 12))

    # Summary
    story.append(KeepTogether([Paragraph("Summary", subtitle_style), Paragraph(data['summary'], normal_style), Spacer(1, 12)]))

    # Technical Proficiency
    story.append(KeepTogether([Paragraph("Technical Proficiency", subtitle_style)]))
    for key, value in data['technical_proficiency'].items():
        story.append(KeepTogether([Paragraph(f"<b>{key.replace('_', ' ').title()}:</b> {value}", normal_style)]))
    story.append(Spacer(1, 12))

    # Experience
    story.append(Paragraph("Experience", subtitle_style))
    for exp in data['experience']:
        exp_details = [
            Paragraph(f"<b>{exp['position']}</b> @ {exp['company']} ({exp['dates']})", normal_style)
        ]
        for responsibility in exp['responsibilities']:
            exp_details.append(Paragraph(f"• {responsibility}", bullet_style))
        story.append(KeepTogether(exp_details))
        story.append(Spacer(1, 6))
    story.append(Spacer(1, 12))

    # Projects
    story.append(Paragraph("Projects", subtitle_style))
    for project in data['projects']:
        project_details = [
            Paragraph(f"<b>{project['title']}</b> (<a href='{project['url']}' color='blue'>{project['url']}</a>)", normal_style),
            Paragraph(project['description'], normal_style),
            Paragraph(f"Technologies: {project['technologies']}", normal_style)
        ]
        story.append(KeepTogether(project_details))
        story.append(Spacer(1, 6))
    story.append(Spacer(1, 12))

    # Education
    story.append(Paragraph("Education", subtitle_style))
    for edu in data['education']:
        story.append(KeepTogether([Paragraph(f"<b>{edu['degree']}</b>, {edu['institution']} ({edu['dates']})", normal_style)]))
        story.append(Spacer(1, 6))
    story.append(Spacer(1, 12))

    # Additional Experience
    story.append(Paragraph("Additional Experience", subtitle_style))
    for add_exp in data['additional_experience']:
        add_exp_details = [
            Paragraph(f"<b>{add_exp['position']}</b> @ {add_exp['company']} ({add_exp['dates']})", normal_style)
        ]
        for responsibility in add_exp['responsibilities']:
            add_exp_details.append(Paragraph(f"• {responsibility}", bullet_style))
        story.append(KeepTogether(add_exp_details))
        story.append(Spacer(1, 6))
    story.append(Spacer(1, 12))

    # Skills
    story.append(Paragraph("Skills", subtitle_style))
    skill_items = [Paragraph(f"• {skill}", bullet_style) for skill in data['skills']]
    skills_table = Table([skill_items[i:i+3] for i in range(0, len(skill_items), 3)], hAlign='LEFT')
    story.append(KeepTogether([skills_table]))

    # Build the PDF
    doc.build(story)

if __name__ == "__main__":
    resume_data = load_resume_data("resume_data.json")
    generate_resume(resume_data)
