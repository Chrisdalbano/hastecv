from reportlab.lib.styles import ParagraphStyle
from styles.base_styles import get_base_styles
from styles.colors import TEMPLATE_COLORS

def get_custom_styles(template="default"):
    base_styles = get_base_styles()
    colors = TEMPLATE_COLORS.get(template)

    custom_title_style = ParagraphStyle(
        name='CustomTitle',
        parent=base_styles['BaseTitle'],
        textColor=colors['title']
    )

    custom_subtitleh2_style = ParagraphStyle(
        name='CustomSubtitle',
        parent=base_styles['BaseTitle'],
        fontSize=16,
        textColor=colors['h2']
    )
    
    custom_h2_style = ParagraphStyle(
        name='CustomH2',
        parent=base_styles['BaseTitle'],
        fontSize=16,
        textColor=colors['h2']
    )

    custom_normal_style = ParagraphStyle(
        name='CustomNormal',
        parent=base_styles['BaseNormal'],
        textColor=colors['normal_text']
    )

    custom_bold_style = ParagraphStyle(
        name='CustomBold',
        parent=base_styles['BaseBold'],
        textColor=colors['normal_text']
    )

    custom_bullet_style = ParagraphStyle(
        name='CustomBullet',
        parent=base_styles['BaseBullet'],
        textColor=colors['normal_text']
    )

    return {
        'CustomTitle': custom_title_style,
        'CustomH2': custom_h2_style,
        'CustomNormal': custom_normal_style,
        'CustomBold': custom_bold_style,
        'CustomBullet': custom_bullet_style,
        'CustomSubtitle': custom_subtitleh2_style,
    }
