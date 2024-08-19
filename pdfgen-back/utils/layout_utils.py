from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle

def create_contact_table(contact_data, icon_size, styles):
    contact_grid_data = []
    for i in range(0, len(contact_data), 2):
        if i + 1 < len(contact_data):
            contact_grid_data.append(contact_data[i] + contact_data[i + 1])
        else:
            contact_grid_data.append(contact_data[i])

    contact_table = Table(contact_grid_data, hAlign='CENTER', colWidths=[icon_size, 6, 2.4 * inch, icon_size, 6, 2.4 * inch])
    contact_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'OpenSans-Regular'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))

    return contact_table
