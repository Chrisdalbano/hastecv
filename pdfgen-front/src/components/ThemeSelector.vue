<template>
  <div class="theme-selector">
    <div class="selector-header">
      <h3 class="selector-title">Resume Color Theme</h3>
      <p class="selector-description">Choose a professional color theme for your PDF resume</p>
    </div>

    <!-- Theme Grid -->
    <div class="themes-grid">
      <button
        v-for="(theme, key) in themeStore.pdfThemes"
        :key="key"
        :class="['theme-card', { 
          'theme-active': themeStore.pdfTheme === key && !themeStore.pdfCustomColor 
        }]"
        @click="selectTheme(key)"
        :title="theme.description + ' - ' + theme.personality"
      >
        <div class="theme-color-bar" :style="{ background: theme.gradient }"></div>
        <div class="theme-content">
          <div class="theme-name">{{ theme.name }}</div>
          <div class="theme-meta">{{ theme.personality.split(',')[0] }}</div>
        </div>
        <div v-if="themeStore.pdfTheme === key && !themeStore.pdfCustomColor" class="theme-check">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M13.3333 4L6 11.3333L2.66667 8" 
                  stroke="currentColor" 
                  stroke-width="2" 
                  stroke-linecap="round" 
                  stroke-linejoin="round"/>
          </svg>
        </div>
      </button>
    </div>

    <!-- Custom Color Picker -->
    <div class="custom-color-section">
      <div class="section-divider">
        <span class="divider-text">Custom Color</span>
      </div>
      
      <div class="color-picker-container">
        <div class="color-input-wrapper">
          <label class="color-label">Choose Custom Color</label>
          <div class="color-input-group">
            <input
              type="color"
              v-model="localCustomColor"
              @input="onColorChange"
              class="color-input"
            />
            <input
              type="text"
              v-model="localCustomColor"
              @input="onColorChange"
              placeholder="#000000"
              class="color-text-input"
              pattern="^#[0-9A-Fa-f]{6}$"
            />
            <button
              v-if="themeStore.customColor"
              @click="clearCustom"
              class="clear-button"
              title="Clear custom color"
            >
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                <path d="M12 4L4 12M4 4L12 12" 
                      stroke="currentColor" 
                      stroke-width="2" 
                      stroke-linecap="round"/>
              </svg>
            </button>
          </div>
          <p class="color-help-text">
            Custom colors will be applied to your PDF resume output
          </p>
        </div>

        <!-- Live Preview -->
        <div v-if="themeStore.pdfCustomColor" class="color-preview-card">
          <div class="preview-header">
            <span>PDF Color Preview</span>
          </div>
          <div class="preview-elements">
            <button class="preview-button" :style="{ 
              borderColor: themeStore.pdfCustomColor,
              color: themeStore.pdfCustomColor
            }">
              Heading Style
            </button>
            <div class="preview-badge" :style="{ 
              backgroundColor: themeStore.pdfCustomColor 
            }">
              Accent
            </div>
            <div class="preview-text" :style="{ color: themeStore.pdfCustomColor }">
              Section Title
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useThemeStore } from '../stores/themeStore';

const themeStore = useThemeStore();
const localCustomColor = ref(themeStore.pdfCustomColor || '#1E3A8A');

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

watch(() => themeStore.pdfCustomColor, (newValue) => {
  if (newValue) {
    localCustomColor.value = newValue;
  }
});
</script>

<style scoped>
.theme-selector {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1rem;
  background: transparent;
}

/* Header */
.selector-header {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.selector-title {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: white;
  letter-spacing: -0.01em;
}

.selector-description {
  margin: 0;
  font-size: 0.875rem;
  color: var(--gray-400);
  line-height: 1.5;
}

/* Themes Grid */
.themes-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.5rem;
}

.theme-card {
  position: relative;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  background: var(--gray-800);
  border: 2px solid var(--gray-700);
  border-radius: 6px;
  padding: 0.75rem;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.theme-card:hover {
  border-color: var(--haste-primary);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.theme-active {
  border-color: var(--haste-primary);
  background: rgba(var(--haste-primary-rgb), 0.1);
}

.theme-color-bar {
  width: 4px;
  height: 40px;
  border-radius: 2px;
  flex-shrink: 0;
}

.theme-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  min-width: 0;
}

.theme-name {
  font-size: 0.875rem;
  font-weight: 600;
  color: white;
  letter-spacing: -0.01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.theme-meta {
  font-size: 0.75rem;
  color: var(--gray-400);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.theme-check {
  width: 20px;
  height: 20px;
  background: var(--haste-primary);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

/* Custom Color Section */
.custom-color-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.section-divider {
  position: relative;
  text-align: center;
  margin: 1rem 0;
}

.section-divider::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  height: 1px;
  background: var(--gray-700);
}

.divider-text {
  position: relative;
  background: var(--gray-900);
  padding: 0 1rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--gray-400);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.color-picker-container {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 1.5rem;
  align-items: start;
}

.color-input-wrapper {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.color-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: white;
}

.color-input-group {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.color-input {
  width: 60px;
  height: 44px;
  border: 2px solid var(--border-color);
  border-radius: 8px;
  cursor: pointer;
  background: var(--gray-800);
  transition: border-color 0.2s;
}

.color-input:hover {
  border-color: var(--haste-primary);
}

.color-text-input {
  flex: 1;
  height: 44px;
  padding: 0 1rem;
  background: var(--gray-800);
  border: 2px solid var(--border-color);
  border-radius: 8px;
  color: white;
  font-size: 0.875rem;
  font-family: 'Courier New', monospace;
  text-transform: uppercase;
  transition: all 0.2s;
}

.color-text-input:focus {
  outline: none;
  border-color: var(--haste-primary);
  box-shadow: 0 0 0 3px rgba(var(--haste-primary-rgb), 0.1);
}

.clear-button {
  width: 44px;
  height: 44px;
  background: var(--gray-800);
  border: 2px solid var(--border-color);
  border-radius: 8px;
  color: var(--gray-400);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.clear-button:hover {
  background: #dc2626;
  border-color: #dc2626;
  color: white;
}

.color-help-text {
  margin: 0;
  font-size: 0.75rem;
  color: var(--gray-500);
  line-height: 1.5;
}

/* Live Preview Card */
.color-preview-card {
  background: var(--gray-800);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 1rem;
  min-width: 200px;
}

.preview-header {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--gray-400);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.75rem;
}

.preview-elements {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.preview-button {
  padding: 0.5rem 1rem;
  border: 2px solid;
  border-radius: 6px;
  background: transparent;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: default;
  transition: all 0.2s;
}

.preview-badge {
  padding: 0.375rem 0.75rem;
  border-radius: 6px;
  font-size: 0.8125rem;
  font-weight: 600;
  color: white;
  text-align: center;
}

.preview-text {
  font-size: 0.875rem;
  font-weight: 600;
}

/* Responsive */
@media (max-width: 1024px) {
  .themes-grid {
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  }

  .color-picker-container {
    grid-template-columns: 1fr;
  }

  .color-preview-card {
    min-width: auto;
  }
}

@media (max-width: 768px) {
  .themes-grid {
    grid-template-columns: 1fr;
  }

  .theme-selector {
    padding: 1rem;
  }
}
</style>

