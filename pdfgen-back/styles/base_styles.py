from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from styles.fonts import register_fonts
from styles.colors import TEMPLATE_COLORS

def get_base_styles():
    register_fonts()
    styles = getSampleStyleSheet()

    base_title_style = ParagraphStyle(
        name='BaseTitle',
        parent=styles['Title'],
        fontName='Lexend-Bold',
        fontSize=18,
        leading=22,
        spaceAfter=14,
    )

    base_normal_style = ParagraphStyle(
        name='BaseNormal',
        parent=styles['Normal'],
        fontName='OpenSans-Regular',
        fontSize=10,
        leading=12,
    )

    base_bold_style = ParagraphStyle(
        name='BaseBold',
        parent=styles['Normal'],
        fontName='OpenSans-Bold',
        fontSize=10,
        leading=12,
    )

    base_bullet_style = ParagraphStyle(
        name='BaseBullet',
        parent=styles['Normal'],
        fontName='OpenSans-Regular',
        fontSize=10,
        leading=12,
        leftIndent=10,
        bulletFontName='OpenSans-Regular',
        bulletIndent=0
    )

    return {
        'BaseTitle': base_title_style,
        'BaseNormal': base_normal_style,
        'BaseBold': base_bold_style,
        'BaseBullet': base_bullet_style
    }
