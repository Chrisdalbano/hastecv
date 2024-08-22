import os
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def register_fonts():
    font_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static', 'fonts'))

    fonts = {
        'OpenSans-Regular': 'OpenSans-VariableFont_wdth,wght.ttf',
        'OpenSans-Bold': 'OpenSans-Bold.ttf',
        'OpenSans-Italic': 'OpenSans-Italic-VariableFont_wdth,wght.ttf',
        'Lexend-Bold': 'Lexend-Bold.ttf'
    }

    for font_name, font_file in fonts.items():
        font_path = os.path.join(font_dir, font_file)
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found: {font_path}")
        pdfmetrics.registerFont(TTFont(font_name, font_path))

    return fonts
