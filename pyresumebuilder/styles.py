import os
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics




def get_styles():
    styles = getSampleStyleSheet()

    # Correct font paths
    font_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'fonts'))
    regular_font_path = os.path.join(font_dir, 'OpenSans-VariableFont_wdth,wght.ttf')
    bold_font_path = os.path.join(font_dir, 'OpenSans-Bold.ttf')
    italic_font_path = os.path.join(font_dir, 'OpenSans-Italic-VariableFont_wdth,wght.ttf')
    lexend_font_path = os.path.join(font_dir, 'Lexend-Bold.ttf')

    # Check if font files exist
    if not os.path.exists(regular_font_path):
        raise FileNotFoundError(f"Font file not found: {regular_font_path}")
    if not os.path.exists(italic_font_path):
        raise FileNotFoundError(f"Font file not found: {italic_font_path}")
    if not os.path.exists(bold_font_path):
        raise FileNotFoundError(f"Font file not found: {bold_font_path}")
    if not os.path.exists(lexend_font_path):
        raise FileNotFoundError(f"Font file not found: {lexend_font_path}")

    # Custom fonts
    pdfmetrics.registerFont(TTFont('OpenSans-Regular', regular_font_path))
    pdfmetrics.registerFont(TTFont('OpenSans-Bold', bold_font_path))
    pdfmetrics.registerFont(TTFont('OpenSans-Italic', italic_font_path))
    pdfmetrics.registerFont(TTFont('Lexend-Bold', lexend_font_path))

    # Custom styles
    custom_title_style = ParagraphStyle(
        name='CustomTitle',
        parent=styles['Title'],
        fontName='Lexend-Bold',
        fontSize=18,
        leading=22,
        spaceAfter=14,
        textColor=colors.white
    )

    custom_h2_style = ParagraphStyle(
        name='CustomH2',
        parent=styles['Title'],
        fontName='Lexend-Bold',
        fontSize=18,
        leading=22,
        spaceAfter=14,
        textColor=colors.orange
    )

    custom_subtitle_style = ParagraphStyle(
        name='CustomSubtitle',
        parent=styles['Heading2'],
        fontName='Lexend-Bold',
        fontSize=12,
        leading=18,
        textColor=colors.HexColor('#262626'),
        spaceBefore=12,
        spaceAfter=6
    )

    custom_normal_style = ParagraphStyle(
        name='CustomNormal',
        parent=styles['Normal'],
        fontName='OpenSans-Regular',
        fontSize=10,
        leading=12,
        textColor=colors.HexColor('#262626')
    )

   

    custom_bold_style = ParagraphStyle(
        name='CustomBold',
        parent=styles['Normal'],
        fontName='OpenSans-Bold',
        fontSize=10,
        leading=12,
        # textcolor=colors.HexColor('#007AFF')
        textColor=colors.HexColor('#262626'),
    )


    custom_bullet_style = ParagraphStyle(
        name='CustomBullet',
        parent=styles['Normal'],
        fontName='OpenSans-Regular',
        fontSize=10,
        leading=12,
        textColor=colors.HexColor('#262626'),
        leftIndent=10,
        bulletFontName='OpenSans-Regular',
        bulletIndent=0
    )


    # Add or replace styles
    styles.add(custom_title_style)
    styles.add(custom_h2_style)
    styles.add(custom_subtitle_style)
    styles.add(custom_normal_style)
    styles.add(custom_bullet_style)
    styles.add(custom_bold_style)

    return styles
