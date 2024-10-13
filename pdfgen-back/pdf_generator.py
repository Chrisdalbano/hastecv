import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    KeepTogether,
    Image,
    Table,
    TableStyle,
)
from reportlab.lib import colors
from styles.custom_styles import get_custom_styles
from styles.colors import TEMPLATE_COLORS


def generate_resume(data, template="minimal"):
    doc = SimpleDocTemplate("resume.pdf", pagesize=letter)
    styles = get_custom_styles(template)
    story = []

    # Set global icon size and text gap
    icon_size = 11
    icon_text_gap = 6

    # Define header background drawing function
    header_bg_color = TEMPLATE_COLORS.get(template, {}).get("header_bg", None)
    header_height = 1 * inch

    def draw_header_background(canvas, doc):
        if header_bg_color:
            canvas.saveState()
            canvas.setFillColorRGB(
                header_bg_color.red, header_bg_color.green, header_bg_color.blue
            )
            canvas.rect(
                0,
                doc.height + doc.topMargin - header_height,
                doc.width,
                header_height,
                fill=1,
            )
            canvas.restoreState()

    # Add header content
    def add_header_content():
        header_content = [
            Paragraph(data.get("name", ""), styles["CustomTitle"]),
            Spacer(1, 2),
        ]
        if "title" in data:
            header_content.append(
                Paragraph(data.get("title", ""), styles["CustomSubtitle"])
            )
        story.append(KeepTogether(header_content))

    # Add contact information as a table
    def add_contact_info():
        icons_path = "static/icons"
        contact_items = [
            ("email.png", data.get("contact", {}).get("email")),
            ("linkedin.png", data.get("contact", {}).get("linkedin")),
            ("location.png", data.get("contact", {}).get("location")),
            ("github.png", data.get("contact", {}).get("github")),
            ("phone.png", data.get("contact", {}).get("phone")),
            ("website.png", data.get("contact", {}).get("website")),
        ]

        def create_contact_row(icon_filename, text, link=None):
            if not text:
                return None
            icon_path = os.path.join(icons_path, icon_filename)
            return [
                Image(icon_path, width=icon_size, height=icon_size),
                Spacer(icon_text_gap, 0),
                Paragraph(text, styles["CustomNormal"]),
            ]

        contact_data = [
            create_contact_row(icon, text) for icon, text in contact_items if text
        ]

        # Arrange contact data in a 2x3 grid
        contact_rows = [contact_data[i : i + 2] for i in range(0, len(contact_data), 2)]
        contact_table = Table(
            [sum(row, []) for row in contact_rows],
            hAlign="CENTER",
            colWidths=[icon_size, icon_text_gap, 2.4 * inch] * 2,
        )
        contact_table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                    ("FONTNAME", (0, 0), (-1, -1), "OpenSans-Regular"),
                    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                ]
            )
        )
        story.append(contact_table)
        story.append(Spacer(1, 20))

    # Add generic section
    def add_section(title, content, custom_style=None):
        if not content:
            return
        story.append(Paragraph(title, custom_style or styles["CustomH2"]))

        # Handle content as list or string
        if isinstance(content, list):
            for item in content:
                story.append(Paragraph(f"• {item}", styles["CustomBullet"]))
                story.append(Spacer(1, 6))
        else:
            story.append(Paragraph(content, styles["CustomNormal"]))
            story.append(Spacer(1, 12))

    # Add experience section
    def add_experience_section():
        story.append(Paragraph("Experience", styles["CustomH2"]))

        for exp in data.get("experience", []):
            story.append(
                Paragraph(
                    f"<b>{exp['position']}</b> @ {exp['company']} ({exp['dates']})",
                    styles["CustomBold"],
                )
            )

            responsibilities = exp.get("responsibilities", [])
            # Ensure responsibilities is treated as a list
            if isinstance(responsibilities, str):
                responsibilities = responsibilities.split("\n")

            if responsibilities:
                for responsibility in responsibilities:
                    responsibility = responsibility.strip()
                    if responsibility:
                        story.append(
                            Paragraph(f"• {responsibility}", styles["CustomBullet"])
                        )
            story.append(Spacer(1, 12))

    # Add education section
    def add_education_section():
        story.append(Paragraph("Education", styles["CustomH2"]))
        for edu in data.get("education", []):
            story.append(
                Paragraph(
                    f"<b>{edu['degree']}</b>, {edu['institution']} ({edu['dates']})",
                    styles["CustomNormal"],
                )
            )
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 12))

    # Add projects section
    def add_projects_section():
        story.append(Paragraph("Projects", styles["CustomH2"]))
        url_color = "#63C5DA" if template == "modern" else "darkorange"
        for project in data.get("projects", []):
            story.append(
                Paragraph(
                    f"<b>{project['title']}</b> (<a href='{project['url']}' color='{url_color}'>{project['url']}</a>)",
                    styles["CustomBold"],
                )
            )
            story.append(Paragraph(project["description"], styles["CustomNormal"]))
            story.append(
                Paragraph(
                    f"Technologies: {project['technologies']}", styles["CustomNormal"]
                )
            )
            story.append(Spacer(1, 6))
        story.append(Spacer(1, 12))

    # Add technical proficiency section
    def add_technical_proficiency_section():
        if data.get("technical_proficiency", {}):
            story.append(Paragraph("Technical Proficiency", styles["CustomH2"]))
            for key, value in data.get("technical_proficiency", {}).items():
                formatted_key = key.replace("_", " ").title()
                story.append(Paragraph(f"{formatted_key}:", styles["CustomBold"]))
                story.append(Paragraph(value, styles["CustomNormal"]))
                story.append(Spacer(1, 6))
            story.append(Spacer(1, 12))

    # Add sections to the document
    add_header_content()
    add_contact_info()
    add_section(
        "Summary", data.get("summary", [])
    )  # Handle summary as a list or string
    add_technical_proficiency_section()
    add_experience_section()
    add_projects_section()
    add_education_section()
    add_section("Skills", data.get("skills", []))  # Handle skills

    # Build the PDF document
    build_method = (
        doc.build
        if template == "minimal"
        else lambda s: doc.build(s, onFirstPage=draw_header_background)
    )
    build_method(story)


if __name__ == "__main__":
    data = {}
    generate_resume(data, template="default")
