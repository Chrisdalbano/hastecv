import { defineStore } from 'pinia';
import { ref, watch } from 'vue';

export const useThemeStore = defineStore('theme', () => {
  // App UI theme (keep as red for now)
  const currentTheme = ref('professional-red');
  
  // PDF-specific theme selection
  const pdfTheme = ref('professional-navy');
  const pdfCustomColor = ref(null);
  
  // App UI themes (original)
  const themes = {
    'professional-red': {
      name: 'Professional Red',
      primary: '#FF453A',
      primaryRgb: '255, 69, 58',
      gradient: 'linear-gradient(135deg, #FF453A, #d13639)',
      description: 'Bold and confident'
    },
    'corporate-blue': {
      name: 'Corporate Blue',
      primary: '#0066CC',
      primaryRgb: '0, 102, 204',
      gradient: 'linear-gradient(135deg, #0066CC, #004C99)',
      description: 'Professional and trustworthy'
    },
    'modern-purple': {
      name: 'Modern Purple',
      primary: '#8B5CF6',
      primaryRgb: '139, 92, 246',
      gradient: 'linear-gradient(135deg, #8B5CF6, #7C3AED)',
      description: 'Creative and modern'
    },
    'elegant-green': {
      name: 'Elegant Green',
      primary: '#10B981',
      primaryRgb: '16, 185, 129',
      gradient: 'linear-gradient(135deg, #10B981, #059669)',
      description: 'Fresh and balanced'
    },
    'executive-gold': {
      name: 'Executive Gold',
      primary: '#F59E0B',
      primaryRgb: '245, 158, 11',
      gradient: 'linear-gradient(135deg, #F59E0B, #D97706)',
      description: 'Luxurious and prestigious'
    },
    'minimal-gray': {
      name: 'Minimal Gray',
      primary: '#6B7280',
      primaryRgb: '107, 114, 128',
      gradient: 'linear-gradient(135deg, #6B7280, #4B5563)',
      description: 'Clean and minimal'
    }
  };
  
  // PDF-specific themes (for resume output)
  const pdfThemes = {
    'professional-navy': {
      name: 'Professional Navy',
      primary: '#1E3A8A',
      primaryRgb: '30, 58, 138',
      gradient: 'linear-gradient(135deg, #1E3A8A, #3B82F6)',
      description: 'Trustworthy and authoritative',
      personality: 'Corporate, Finance, Legal',
      contrast: 'AAA'
    },
    'executive-burgundy': {
      name: 'Executive Burgundy',
      primary: '#881337',
      primaryRgb: '136, 19, 55',
      gradient: 'linear-gradient(135deg, #881337, #BE123C)',
      description: 'Sophisticated and powerful',
      personality: 'Executive, Management, Leadership',
      contrast: 'AAA'
    },
    'creative-teal': {
      name: 'Creative Teal',
      primary: '#0F766E',
      primaryRgb: '15, 118, 110',
      gradient: 'linear-gradient(135deg, #0F766E, #14B8A6)',
      description: 'Innovative and balanced',
      personality: 'Design, Marketing, Creative',
      contrast: 'AAA'
    },
    'modern-slate': {
      name: 'Modern Slate',
      primary: '#334155',
      primaryRgb: '51, 65, 85',
      gradient: 'linear-gradient(135deg, #334155, #64748B)',
      description: 'Minimal and contemporary',
      personality: 'Tech, Engineering, Architecture',
      contrast: 'AAA'
    },
    'academic-emerald': {
      name: 'Academic Emerald',
      primary: '#065F46',
      primaryRgb: '6, 95, 70',
      gradient: 'linear-gradient(135deg, #065F46, #059669)',
      description: 'Professional and growth-oriented',
      personality: 'Education, Research, Healthcare',
      contrast: 'AAA'
    }
  };

  // Get app UI theme
  const getTheme = () => themes[currentTheme.value];
  
  // Get PDF theme
  const getPDFTheme = () => pdfThemes[pdfTheme.value];

  // Get active PDF color (custom or theme)
  const getPDFColor = () => {
    if (pdfCustomColor.value) {
      return pdfCustomColor.value;
    }
    return pdfThemes[pdfTheme.value]?.primary || '#1E3A8A';
  };

  // Convert hex to RGB string
  function hexToRgb(hex) {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result
      ? `${parseInt(result[1], 16)}, ${parseInt(result[2], 16)}, ${parseInt(result[3], 16)}`
      : '0, 0, 0';
  }

  // Apply app UI theme to CSS variables
  function applyTheme() {
    const theme = getTheme();
    const root = document.documentElement;
    
    root.style.setProperty('--haste-primary', theme.primary);
    root.style.setProperty('--haste-primary-rgb', theme.primaryRgb);
    root.style.setProperty('--haste-gradient', theme.gradient);
    root.style.setProperty('--border-color', `rgba(${theme.primaryRgb}, 0.3)`);
    root.style.setProperty('--hover-color', `rgba(${theme.primaryRgb}, 0.1)`);
    
    // Legacy support
    root.style.setProperty('--haste-yellow', theme.primary);
    root.style.setProperty('--haste-red', theme.primary);
  }

  // Watch for app theme changes
  watch(currentTheme, () => {
    applyTheme();
    localStorage.setItem('hastecv-theme', currentTheme.value);
  });

  // Watch for PDF theme changes
  watch(pdfTheme, () => {
    localStorage.setItem('hastecv-pdf-theme', pdfTheme.value);
  });

  // Watch for PDF custom color changes
  watch(pdfCustomColor, () => {
    if (pdfCustomColor.value) {
      localStorage.setItem('hastecv-pdf-custom-color', pdfCustomColor.value);
    } else {
      localStorage.removeItem('hastecv-pdf-custom-color');
    }
  });

  // Load themes from localStorage
  function loadTheme() {
    const savedTheme = localStorage.getItem('hastecv-theme');
    const savedPDFTheme = localStorage.getItem('hastecv-pdf-theme');
    const savedPDFCustom = localStorage.getItem('hastecv-pdf-custom-color');
    
    if (savedTheme && themes[savedTheme]) {
      currentTheme.value = savedTheme;
    }
    
    if (savedPDFTheme && pdfThemes[savedPDFTheme]) {
      pdfTheme.value = savedPDFTheme;
    }
    
    if (savedPDFCustom) {
      pdfCustomColor.value = savedPDFCustom;
    }
    
    applyTheme();
  }

  // Set app UI theme
  function setTheme(themeKey) {
    if (themes[themeKey]) {
      currentTheme.value = themeKey;
    }
  }

  // Set PDF theme
  function setPDFTheme(themeKey) {
    if (pdfThemes[themeKey]) {
      pdfTheme.value = themeKey;
      pdfCustomColor.value = null; // Reset custom color when switching themes
    }
  }

  // Set PDF custom color
  function setPDFCustomColor(color) {
    pdfCustomColor.value = color;
  }

  // Clear PDF custom color
  function clearPDFCustomColor() {
    pdfCustomColor.value = null;
  }

  return {
    // App UI theme
    currentTheme,
    themes,
    getTheme,
    applyTheme,
    loadTheme,
    setTheme,
    // PDF theme
    pdfTheme,
    pdfCustomColor,
    pdfThemes,
    getPDFTheme,
    getPDFColor,
    setPDFTheme,
    setPDFCustomColor,
    clearPDFCustomColor
  };
});

