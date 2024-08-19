from reportlab.lib import colors

TEMPLATE_COLORS = {
    'default': {
        'header_bg': colors.HexColor('#262626'),
        'title': colors.white,
        'h2': colors.orange,
        'normal_text': colors.HexColor('#262626')
    },
    'modern': {
        'header_bg': colors.HexColor('#333333'),
        'title': colors.HexColor('#F5F5F5'),
        'h2': colors.HexColor('#63C5DA'),
        'normal_text': colors.HexColor('#555555')
    },
    'minimal': {
        'header_bg': colors.HexColor('#FFFFFF'),
        'title': colors.HexColor('#000000'),
        'h2': colors.HexColor('#444444'),
        'normal_text': colors.HexColor('#000000')
    }
}

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
