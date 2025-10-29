<template>
  <div :class="['customization-sidebar', { 'is-open': isOpen }]">
    <!-- Mini Icons (Visible when collapsed) -->
    <div v-if="!isOpen" class="mini-icons">
      <button 
        class="mini-icon"
        @click="isOpen = true; activeSection = 'color'"
        title="Theme Color"
      >
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="1.5"/>
          <path d="M10 3v14M17 10H3" stroke="currentColor" stroke-width="1.5"/>
        </svg>
      </button>
      <button 
        class="mini-icon"
        @click="isOpen = true; activeSection = 'spacing'"
        title="Spacing"
      >
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <rect x="3" y="3" width="14" height="3" fill="currentColor"/>
          <rect x="3" y="8.5" width="14" height="3" fill="currentColor"/>
          <rect x="3" y="14" width="14" height="3" fill="currentColor"/>
        </svg>
      </button>
      <button 
        class="mini-icon"
        @click="isOpen = true; activeSection = 'alignment'"
        title="Alignment"
      >
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <path d="M3 4h14M3 10h14M3 16h10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        </svg>
      </button>
      <button 
        class="mini-icon"
        @click="isOpen = true; activeSection = 'margins'"
        title="Margins"
      >
        <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
          <rect x="2" y="2" width="16" height="16" stroke="currentColor" stroke-width="1.5" fill="none"/>
          <rect x="5" y="5" width="10" height="10" fill="currentColor" opacity="0.3"/>
        </svg>
      </button>
    </div>

    <!-- Sidebar Content -->
    <div v-if="isOpen" class="sidebar-content">
      <div class="sidebar-header">
        <h3>PDF Customization</h3>
        <button 
          class="sidebar-close"
          @click="isOpen = false"
          title="Close"
        >
          <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
            <path d="M15 5L5 15M5 5l10 10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
      </div>

      <!-- Color Theme Section -->
      <div class="customization-section">
        <button 
          class="section-toggle"
          @click="toggleSection('color')"
          :class="{ 'active': activeSection === 'color' }"
        >
          <div class="section-icon">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="1.5"/>
              <path d="M10 3v14M17 10H3" stroke="currentColor" stroke-width="1.5"/>
            </svg>
          </div>
          <span class="section-label">Theme Color</span>
          <svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M4 6l4 4 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
        
        <div v-if="activeSection === 'color'" class="section-content">
          <p class="section-description">Choose a professional color for headers and accents</p>
          
          <!-- Color Presets -->
          <div class="color-grid">
            <button
              v-for="(theme, key) in themeStore.pdfThemes"
              :key="key"
              :class="['color-option', { 'active': themeStore.pdfTheme === key && !themeStore.pdfCustomColor }]"
              @click="selectTheme(key)"
              :style="{ '--theme-color': theme.primary }"
            >
              <div class="color-preview"></div>
              <span class="color-name">{{ theme.name }}</span>
            </button>
          </div>

          <!-- Custom Color -->
          <div class="custom-color">
            <label class="custom-label">Custom Color</label>
            <div class="custom-input-group">
              <input
                type="color"
                v-model="localCustomColor"
                @input="onColorChange"
                class="color-picker"
              />
              <input
                type="text"
                v-model="localCustomColor"
                @input="onColorChange"
                pattern="^#[0-9A-Fa-f]{6}$"
                placeholder="#1E3A8A"
                class="color-text"
              />
              <button v-if="themeStore.pdfCustomColor" @click="clearCustom" class="clear-btn">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                  <path d="M12 4L4 12M4 4l8 8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Spacing Section -->
      <div class="customization-section">
        <button 
          class="section-toggle"
          @click="toggleSection('spacing')"
          :class="{ 'active': activeSection === 'spacing' }"
        >
          <div class="section-icon">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <rect x="3" y="3" width="14" height="3" fill="currentColor"/>
              <rect x="3" y="8.5" width="14" height="3" fill="currentColor"/>
              <rect x="3" y="14" width="14" height="3" fill="currentColor"/>
            </svg>
          </div>
          <span class="section-label">Spacing</span>
          <svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M4 6l4 4 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
        
        <div v-if="activeSection === 'spacing'" class="section-content">
          <p class="section-description">Adjust space between sections</p>
          
          <div class="radio-group">
            <label v-for="option in spacingOptions" :key="option.value" class="radio-label">
              <input
                type="radio"
                :value="option.value"
                v-model="selectedSpacing"
                name="spacing"
              />
              <span class="radio-text">{{ option.label }}</span>
              <span class="radio-hint">{{ option.hint }}</span>
            </label>
          </div>
        </div>
      </div>

      <!-- Alignment Section -->
      <div class="customization-section">
        <button 
          class="section-toggle"
          @click="toggleSection('alignment')"
          :class="{ 'active': activeSection === 'alignment' }"
        >
          <div class="section-icon">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <path d="M3 4h14M3 10h14M3 16h10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg>
          </div>
          <span class="section-label">Alignment</span>
          <svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M4 6l4 4 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
        
        <div v-if="activeSection === 'alignment'" class="section-content">
          <p class="section-description">Position headers and name</p>
          
          <div class="button-group">
            <button
              v-for="option in alignmentOptions"
              :key="option.value"
              :class="['align-btn', { 'active': selectedAlignment === option.value }]"
              @click="selectedAlignment = option.value"
            >
              <component :is="option.icon" />
              <span>{{ option.label }}</span>
            </button>
          </div>
        </div>
      </div>

      <!-- Margins Section -->
      <div class="customization-section">
        <button 
          class="section-toggle"
          @click="toggleSection('margins')"
          :class="{ 'active': activeSection === 'margins' }"
        >
          <div class="section-icon">
            <svg width="20" height="20" viewBox="0 0 20 20" fill="none">
              <rect x="2" y="2" width="16" height="16" stroke="currentColor" stroke-width="1.5" fill="none"/>
              <rect x="5" y="5" width="10" height="10" fill="currentColor" opacity="0.3"/>
            </svg>
          </div>
          <span class="section-label">Margins</span>
          <svg class="chevron" width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M4 6l4 4 4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
          </svg>
        </button>
        
        <div v-if="activeSection === 'margins'" class="section-content">
          <p class="section-description">Set page margins</p>
          
          <div class="radio-group">
            <label v-for="option in marginOptions" :key="option.value" class="radio-label">
              <input
                type="radio"
                :value="option.value"
                v-model="selectedMargin"
                name="margins"
              />
              <span class="radio-text">{{ option.label }}</span>
              <span class="radio-hint">{{ option.hint }}</span>
            </label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, defineComponent, h } from 'vue';
import { useThemeStore } from '../stores/themeStore';

const themeStore = useThemeStore();

// State
const isOpen = ref(false);
const activeSection = ref('color'); // Default open section
const localCustomColor = ref(themeStore.pdfCustomColor || '#1E3A8A');
const selectedSpacing = ref('normal');
const selectedAlignment = ref('left');
const selectedMargin = ref('normal');

// Options
const spacingOptions = [
  { value: 'compact', label: 'Compact', hint: 'Tight spacing, more content' },
  { value: 'normal', label: 'Normal', hint: 'Balanced spacing' },
  { value: 'relaxed', label: 'Relaxed', hint: 'Loose spacing, easier to read' }
];

const marginOptions = [
  { value: 'narrow', label: 'Narrow', hint: '0.5" margins' },
  { value: 'normal', label: 'Normal', hint: '0.75" margins' },
  { value: 'wide', label: 'Wide', hint: '1" margins' }
];

// Alignment icons
const LeftAlignIcon = defineComponent({
  render() {
    return h('svg', { width: '20', height: '20', viewBox: '0 0 20 20', fill: 'none' }, [
      h('path', { d: 'M3 4h14M3 8h10M3 12h14M3 16h10', stroke: 'currentColor', 'stroke-width': '1.5', 'stroke-linecap': 'round' })
    ]);
  }
});

const CenterAlignIcon = defineComponent({
  render() {
    return h('svg', { width: '20', height: '20', viewBox: '0 0 20 20', fill: 'none' }, [
      h('path', { d: 'M3 4h14M5 8h10M3 12h14M5 16h10', stroke: 'currentColor', 'stroke-width': '1.5', 'stroke-linecap': 'round' })
    ]);
  }
});

const alignmentOptions = [
  { value: 'left', label: 'Left', icon: LeftAlignIcon },
  { value: 'center', label: 'Center', icon: CenterAlignIcon }
];

// Methods
function toggleSection(section) {
  activeSection.value = activeSection.value === section ? null : section;
}

function selectTheme(themeKey) {
  themeStore.setPDFTheme(themeKey);
}

function onColorChange() {
  if (/^#[0-9A-Fa-f]{6}$/.test(localCustomColor.value)) {
    themeStore.setPDFCustomColor(localCustomColor.value);
  }
}

function clearCustom() {
  themeStore.clearPDFCustomColor();
  localCustomColor.value = themeStore.getPDFTheme().primary;
}

// Watch for custom color changes
watch(() => themeStore.pdfCustomColor, (newValue) => {
  if (newValue) {
    localCustomColor.value = newValue;
  }
});

// Expose settings and state for parent
defineExpose({
  getLayoutSettings: () => ({
    layout: 'single-column', // Always single column now
    spacing: selectedSpacing.value,
    alignment: selectedAlignment.value,
    margin: selectedMargin.value
  }),
  isOpen
});
</script>

<style scoped>
.customization-sidebar {
  height: 100%;
  display: flex;
  flex-direction: column;
  background: var(--gray-900);
  border-left: 1px solid var(--border-color);
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  width: 64px; /* Collapsed width - shows mini icons */
  flex-shrink: 0;
}

.is-open {
  width: 320px;
}

/* Mini Icons (Collapsed State) */
.mini-icons {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  padding: 1rem 0.5rem;
  align-items: center;
}

.mini-icon {
  width: 48px;
  height: 48px;
  background: transparent;
  border: 2px solid var(--border-color);
  border-radius: 8px;
  color: var(--gray-400);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.mini-icon:hover {
  border-color: var(--haste-primary);
  color: var(--haste-primary);
  background: rgba(var(--haste-primary-rgb), 0.1);
  transform: translateX(-2px);
}

/* Sidebar Content (Expanded State) */
.sidebar-content {
  height: 100%;
  overflow-y: auto;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: 1.5rem;
  border-bottom: 1px solid var(--border-color);
  flex-shrink: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.sidebar-header h3 {
  margin: 0;
  color: white;
  font-size: 1.125rem;
  font-weight: 700;
}

.sidebar-close {
  width: 32px;
  height: 32px;
  background: transparent;
  border: 2px solid var(--border-color);
  border-radius: 6px;
  color: var(--gray-400);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  flex-shrink: 0;
}

.sidebar-close:hover {
  border-color: var(--haste-primary);
  color: var(--haste-primary);
  background: rgba(var(--haste-primary-rgb), 0.1);
}

.customization-section {
  border-bottom: 1px solid var(--border-color);
}

.section-toggle {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 1.5rem;
  background: transparent;
  border: none;
  color: var(--gray-300);
  cursor: pointer;
  transition: all 0.2s;
  text-align: left;
}

.section-toggle:hover {
  background: rgba(var(--haste-primary-rgb), 0.1);
  color: white;
}

.section-toggle.active {
  background: rgba(var(--haste-primary-rgb), 0.15);
  color: white;
}

.section-icon {
  width: 24px;
  height: 24px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--haste-primary);
}

.section-label {
  flex: 1;
  font-size: 0.9375rem;
  font-weight: 600;
}

.chevron {
  flex-shrink: 0;
  transition: transform 0.2s;
  color: var(--gray-500);
}

.section-toggle.active .chevron {
  transform: rotate(180deg);
}

.section-content {
  padding: 1rem 1.5rem 1.5rem;
  animation: slideDown 0.2s ease-out;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.section-description {
  margin: 0 0 1rem 0;
  font-size: 0.8125rem;
  color: var(--gray-400);
  line-height: 1.5;
}

/* Color Grid */
.color-grid {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.color-option {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  background: var(--gray-800);
  border: 2px solid var(--gray-700);
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  color: var(--gray-300);
  font-size: 0.875rem;
  min-width: 0;
  width: 100%;
}

.color-option:hover {
  border-color: var(--haste-primary);
  transform: translateY(-1px);
}

.color-option.active {
  border-color: var(--haste-primary);
  background: rgba(var(--haste-primary-rgb), 0.1);
  color: white;
}

.color-preview {
  width: 32px;
  height: 32px;
  border-radius: 6px;
  background: var(--theme-color);
  flex-shrink: 0;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.color-name {
  font-weight: 600;
  flex: 1;
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* Custom Color */
.custom-color {
  padding-top: 1rem;
  border-top: 1px solid var(--border-color);
}

.custom-label {
  display: block;
  margin-bottom: 0.5rem;
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--gray-300);
}

.custom-input-group {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.color-picker {
  width: 40px;
  height: 40px;
  border: 2px solid var(--border-color);
  border-radius: 6px;
  cursor: pointer;
  background: transparent;
}

.color-text {
  flex: 1;
  padding: 0.625rem;
  background: var(--gray-800);
  border: 2px solid var(--border-color);
  border-radius: 6px;
  color: white;
  font-family: 'Courier New', monospace;
  font-size: 0.875rem;
}

.color-text:focus {
  outline: none;
  border-color: var(--haste-primary);
}

.clear-btn {
  width: 40px;
  height: 40px;
  background: var(--gray-800);
  border: 2px solid var(--border-color);
  border-radius: 6px;
  color: var(--gray-400);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.clear-btn:hover {
  border-color: var(--haste-primary);
  color: var(--haste-primary);
}

/* Radio Group */
.radio-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.radio-label {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.75rem;
  background: var(--gray-800);
  border: 2px solid var(--gray-700);
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.radio-label:hover {
  border-color: var(--haste-primary);
}

.radio-label:has(input:checked) {
  border-color: var(--haste-primary);
  background: rgba(var(--haste-primary-rgb), 0.1);
}

.radio-label input[type="radio"] {
  margin-top: 2px;
  accent-color: var(--haste-primary);
}

.radio-text {
  flex: 1;
  font-size: 0.875rem;
  font-weight: 600;
  color: white;
}

.radio-hint {
  display: block;
  font-size: 0.75rem;
  color: var(--gray-400);
  margin-top: 0.25rem;
}

/* Button Group */
.button-group {
  display: flex;
  gap: 0.5rem;
}

.align-btn {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 0.5rem;
  background: var(--gray-800);
  border: 2px solid var(--gray-700);
  border-radius: 6px;
  color: var(--gray-300);
  cursor: pointer;
  transition: all 0.2s;
  font-size: 0.75rem;
  font-weight: 600;
}

.align-btn:hover {
  border-color: var(--haste-primary);
  transform: translateY(-2px);
}

.align-btn.active {
  border-color: var(--haste-primary);
  background: rgba(var(--haste-primary-rgb), 0.1);
  color: var(--haste-primary);
}

/* Scrollbar */
.sidebar-content::-webkit-scrollbar {
  width: 6px;
}

.sidebar-content::-webkit-scrollbar-track {
  background: var(--gray-800);
}

.sidebar-content::-webkit-scrollbar-thumb {
  background: var(--haste-primary);
  border-radius: 3px;
}

/* Responsive */
@media (max-width: 768px) {
  .sidebar-content {
    width: 280px;
  }

  .is-open .sidebar-toggle {
    right: 280px;
  }

  .color-grid {
    grid-template-columns: 1fr;
  }
}
</style>

