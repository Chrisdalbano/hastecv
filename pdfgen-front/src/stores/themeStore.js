import { defineStore } from 'pinia';
import { ref, watch } from 'vue';

export const useThemeStore = defineStore('theme', () => {
  // Default theme
  const currentTheme = ref('professional-red');
  
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

  // Get current theme colors
  const getTheme = () => themes[currentTheme.value];

  // Apply theme to CSS variables
  function applyTheme() {
    const theme = getTheme();
    const root = document.documentElement;
    
    root.style.setProperty('--haste-primary', theme.primary);
    root.style.setProperty('--haste-primary-rgb', theme.primaryRgb);
    root.style.setProperty('--haste-gradient', theme.gradient);
    root.style.setProperty('--border-color', `rgba(${theme.primaryRgb}, 0.3)`);
    root.style.setProperty('--hover-color', `rgba(${theme.primaryRgb}, 0.1)`);
  }

  // Watch for theme changes
  watch(currentTheme, () => {
    applyTheme();
    // Save to localStorage
    localStorage.setItem('hastecv-theme', currentTheme.value);
  });

  // Load theme from localStorage
  function loadTheme() {
    const saved = localStorage.getItem('hastecv-theme');
    if (saved && themes[saved]) {
      currentTheme.value = saved;
    }
    applyTheme();
  }

  // Set theme
  function setTheme(themeKey) {
    if (themes[themeKey]) {
      currentTheme.value = themeKey;
    }
  }

  return {
    currentTheme,
    themes,
    getTheme,
    applyTheme,
    loadTheme,
    setTheme
  };
});

