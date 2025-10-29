<template>
  <div class="layout-selector">
    <div class="selector-header">
      <h3 class="selector-title">Layout Options</h3>
      <p class="selector-description">Choose how sections are arranged in your resume</p>
    </div>

    <!-- Layout Grid -->
    <div class="layouts-grid">
      <button
        v-for="layout in layouts"
        :key="layout.id"
        :class="['layout-card', { 
          'layout-active': currentLayout === layout.id 
        }]"
        @click="selectLayout(layout.id)"
      >
        <div class="layout-visual">
          <component :is="layout.icon" />
        </div>
        <div class="layout-info">
          <div class="layout-name">{{ layout.name }}</div>
          <div class="layout-description">{{ layout.description }}</div>
          <div class="layout-best-for">
            <span class="best-for-label">Best for:</span>
            {{ layout.bestFor }}
          </div>
        </div>
        <div v-if="currentLayout === layout.id" class="layout-checkmark">
          <svg width="18" height="18" viewBox="0 0 20 20" fill="none">
            <path d="M16.6667 5L7.50004 14.1667L3.33337 10" 
                  stroke="currentColor" 
                  stroke-width="2.5" 
                  stroke-linecap="round" 
                  stroke-linejoin="round"/>
          </svg>
        </div>
      </button>
    </div>

    <!-- Advanced Options -->
    <div class="advanced-options">
      <div class="section-divider">
        <span class="divider-text">Spacing & Alignment</span>
      </div>

      <div class="options-grid">
        <!-- Section Spacing -->
        <div class="option-group">
          <label class="option-label">Section Spacing</label>
          <div class="radio-group">
            <label v-for="spacing in spacingOptions" :key="spacing.value" class="radio-option">
              <input
                type="radio"
                :value="spacing.value"
                v-model="selectedSpacing"
                @change="updateSpacing"
                class="radio-input"
              />
              <span class="radio-label">{{ spacing.label }}</span>
            </label>
          </div>
        </div>

        <!-- Text Alignment -->
        <div class="option-group">
          <label class="option-label">Header Alignment</label>
          <div class="button-group">
            <button
              v-for="align in alignmentOptions"
              :key="align.value"
              :class="['align-button', { 'align-active': selectedAlignment === align.value }]"
              @click="selectAlignment(align.value)"
              :title="align.label"
            >
              <component :is="align.icon" />
            </button>
          </div>
        </div>

        <!-- Margins -->
        <div class="option-group">
          <label class="option-label">Page Margins</label>
          <div class="radio-group">
            <label v-for="margin in marginOptions" :key="margin.value" class="radio-option">
              <input
                type="radio"
                :value="margin.value"
                v-model="selectedMargin"
                @change="updateMargin"
                class="radio-input"
              />
              <span class="radio-label">{{ margin.label }}</span>
            </label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineComponent, h } from 'vue';

// Layout Icons (inline SVG components)
const SingleColumnIcon = defineComponent({
  render() {
    return h('svg', { width: '100', height: '120', viewBox: '0 0 100 120', fill: 'none' }, [
      h('rect', { x: '10', y: '10', width: '80', height: '15', fill: 'currentColor', opacity: '0.9' }),
      h('rect', { x: '10', y: '30', width: '80', height: '20', fill: 'currentColor', opacity: '0.7' }),
      h('rect', { x: '10', y: '55', width: '80', height: '25', fill: 'currentColor', opacity: '0.5' }),
      h('rect', { x: '10', y: '85', width: '80', height: '25', fill: 'currentColor', opacity: '0.3' })
    ]);
  }
});

const TwoColumnIcon = defineComponent({
  render() {
    return h('svg', { width: '100', height: '120', viewBox: '0 0 100 120', fill: 'none' }, [
      h('rect', { x: '5', y: '10', width: '90', height: '15', fill: 'currentColor', opacity: '0.9' }),
      h('rect', { x: '5', y: '30', width: '40', height: '80', fill: 'currentColor', opacity: '0.5' }),
      h('rect', { x: '50', y: '30', width: '45', height: '35', fill: 'currentColor', opacity: '0.7' }),
      h('rect', { x: '50', y: '70', width: '45', height: '40', fill: 'currentColor', opacity: '0.3' })
    ]);
  }
});

const SidebarLeftIcon = defineComponent({
  render() {
    return h('svg', { width: '100', height: '120', viewBox: '0 0 100 120', fill: 'none' }, [
      h('rect', { x: '5', y: '10', width: '25', height: '100', fill: 'currentColor', opacity: '0.8' }),
      h('rect', { x: '35', y: '10', width: '60', height: '20', fill: 'currentColor', opacity: '0.7' }),
      h('rect', { x: '35', y: '35', width: '60', height: '25', fill: 'currentColor', opacity: '0.5' }),
      h('rect', { x: '35', y: '65', width: '60', height: '45', fill: 'currentColor', opacity: '0.3' })
    ]);
  }
});

const SidebarRightIcon = defineComponent({
  render() {
    return h('svg', { width: '100', height: '120', viewBox: '0 0 100 120', fill: 'none' }, [
      h('rect', { x: '5', y: '10', width: '60', height: '20', fill: 'currentColor', opacity: '0.7' }),
      h('rect', { x: '5', y: '35', width: '60', height: '25', fill: 'currentColor', opacity: '0.5' }),
      h('rect', { x: '5', y: '65', width: '60', height: '45', fill: 'currentColor', opacity: '0.3' }),
      h('rect', { x: '70', y: '10', width: '25', height: '100', fill: 'currentColor', opacity: '0.8' })
    ]);
  }
});

const GridIcon = defineComponent({
  render() {
    return h('svg', { width: '100', height: '120', viewBox: '0 0 100 120', fill: 'none' }, [
      h('rect', { x: '5', y: '10', width: '90', height: '15', fill: 'currentColor', opacity: '0.9' }),
      h('rect', { x: '5', y: '30', width: '42', height: '38', fill: 'currentColor', opacity: '0.6' }),
      h('rect', { x: '53', y: '30', width: '42', height: '38', fill: 'currentColor', opacity: '0.6' }),
      h('rect', { x: '5', y: '72', width: '42', height: '38', fill: 'currentColor', opacity: '0.4' }),
      h('rect', { x: '53', y: '72', width: '42', height: '38', fill: 'currentColor', opacity: '0.4' })
    ]);
  }
});

// Alignment Icons
const AlignLeftIcon = defineComponent({
  render() {
    return h('svg', { width: '20', height: '20', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor' }, [
      h('line', { x1: '3', y1: '6', x2: '21', y2: '6', 'stroke-width': '2' }),
      h('line', { x1: '3', y1: '12', x2: '15', y2: '12', 'stroke-width': '2' }),
      h('line', { x1: '3', y1: '18', x2: '18', y2: '18', 'stroke-width': '2' })
    ]);
  }
});

const AlignCenterIcon = defineComponent({
  render() {
    return h('svg', { width: '20', height: '20', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor' }, [
      h('line', { x1: '3', y1: '6', x2: '21', y2: '6', 'stroke-width': '2' }),
      h('line', { x1: '6', y1: '12', x2: '18', y2: '12', 'stroke-width': '2' }),
      h('line', { x1: '4', y1: '18', x2: '20', y2: '18', 'stroke-width': '2' })
    ]);
  }
});

const AlignRightIcon = defineComponent({
  render() {
    return h('svg', { width: '20', height: '20', viewBox: '0 0 24 24', fill: 'none', stroke: 'currentColor' }, [
      h('line', { x1: '3', y1: '6', x2: '21', y2: '6', 'stroke-width': '2' }),
      h('line', { x1: '9', y1: '12', x2: '21', y2: '12', 'stroke-width': '2' }),
      h('line', { x1: '6', y1: '18', x2: '21', y2: '18', 'stroke-width': '2' })
    ]);
  }
});

// Layout options
const layouts = [
  {
    id: 'single-column',
    name: 'Single Column',
    description: 'Traditional layout with all sections stacked vertically',
    bestFor: 'Most professions, clean and simple',
    icon: SingleColumnIcon
  },
  {
    id: 'two-column',
    name: 'Two Column',
    description: 'Header on top with content in two balanced columns',
    bestFor: 'Designers, creative professionals',
    icon: TwoColumnIcon
  },
  {
    id: 'sidebar-left',
    name: 'Sidebar Left',
    description: 'Compact sidebar for contact info and skills',
    bestFor: 'Tech, modern industries',
    icon: SidebarLeftIcon
  },
  {
    id: 'sidebar-right',
    name: 'Sidebar Right',
    description: 'Main content on left, sidebar with details on right',
    bestFor: 'Traditional, conservative fields',
    icon: SidebarRightIcon
  },
  {
    id: 'grid',
    name: 'Grid Layout',
    description: 'Sections arranged in a responsive grid pattern',
    bestFor: 'Portfolio, project-heavy resumes',
    icon: GridIcon
  }
];

const spacingOptions = [
  { label: 'Compact', value: 'compact' },
  { label: 'Normal', value: 'normal' },
  { label: 'Relaxed', value: 'relaxed' }
];

const alignmentOptions = [
  { label: 'Left', value: 'left', icon: AlignLeftIcon },
  { label: 'Center', value: 'center', icon: AlignCenterIcon },
  { label: 'Right', value: 'right', icon: AlignRightIcon }
];

const marginOptions = [
  { label: 'Narrow', value: 'narrow' },
  { label: 'Normal', value: 'normal' },
  { label: 'Wide', value: 'wide' }
];

const currentLayout = ref('single-column');
const selectedSpacing = ref('normal');
const selectedAlignment = ref('left');
const selectedMargin = ref('normal');

function selectLayout(layoutId) {
  currentLayout.value = layoutId;
  saveLayoutSettings();
}

function selectAlignment(value) {
  selectedAlignment.value = value;
  saveLayoutSettings();
}

function updateSpacing() {
  saveLayoutSettings();
}

function updateMargin() {
  saveLayoutSettings();
}

function saveLayoutSettings() {
  const settings = {
    layout: currentLayout.value,
    spacing: selectedSpacing.value,
    alignment: selectedAlignment.value,
    margin: selectedMargin.value
  };
  localStorage.setItem('hastecv-layout-settings', JSON.stringify(settings));
}

// Load saved settings
function loadLayoutSettings() {
  const saved = localStorage.getItem('hastecv-layout-settings');
  if (saved) {
    const settings = JSON.parse(saved);
    currentLayout.value = settings.layout || 'single-column';
    selectedSpacing.value = settings.spacing || 'normal';
    selectedAlignment.value = settings.alignment || 'left';
    selectedMargin.value = settings.margin || 'normal';
  }
}

// Load settings on mount
loadLayoutSettings();

// Export for parent components
defineExpose({
  getLayoutSettings: () => ({
    layout: currentLayout.value,
    spacing: selectedSpacing.value,
    alignment: selectedAlignment.value,
    margin: selectedMargin.value
  })
});
</script>

<style scoped>
.layout-selector {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  padding: 1.5rem;
  background: var(--gray-900);
  border: 1px solid var(--border-color);
  border-radius: 12px;
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

/* Layouts Grid */
.layouts-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.5rem;
}

.layout-card {
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

.layout-card:hover {
  border-color: var(--haste-primary);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.layout-active {
  border-color: var(--haste-primary);
  background: rgba(var(--haste-primary-rgb), 0.1);
}

.layout-visual {
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--gray-700), var(--gray-800));
  border-radius: 4px;
  color: var(--gray-400);
  transition: color 0.2s;
  flex-shrink: 0;
}

.layout-card:hover .layout-visual {
  color: var(--haste-primary);
}

.layout-visual svg {
  width: 30px;
  height: 36px;
}

.layout-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  min-width: 0;
}

.layout-name {
  font-size: 0.875rem;
  font-weight: 600;
  color: white;
  letter-spacing: -0.01em;
}

.layout-description {
  font-size: 0.75rem;
  color: var(--gray-400);
  line-height: 1.3;
  display: none; /* Hide description in compact mode */
}

.layout-best-for {
  font-size: 0.7rem;
  color: var(--gray-500);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.best-for-label {
  font-weight: 600;
  color: var(--gray-400);
}

.layout-checkmark {
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

/* Advanced Options */
.advanced-options {
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

.options-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.option-group {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.option-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: white;
}

/* Radio Group */
.radio-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.radio-option {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  background: var(--gray-800);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.radio-option:hover {
  border-color: var(--haste-primary);
  background: var(--gray-700);
}

.radio-input {
  width: 18px;
  height: 18px;
  accent-color: var(--haste-primary);
  cursor: pointer;
}

.radio-label {
  font-size: 0.875rem;
  color: var(--gray-300);
  cursor: pointer;
}

/* Button Group */
.button-group {
  display: flex;
  gap: 0.5rem;
}

.align-button {
  flex: 1;
  height: 44px;
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

.align-button:hover {
  border-color: var(--haste-primary);
  color: var(--haste-primary);
}

.align-active {
  background: var(--haste-primary);
  border-color: var(--haste-primary);
  color: white;
}

/* Responsive */
@media (max-width: 1024px) {
  .layouts-grid {
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  }

  .options-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .layouts-grid {
    grid-template-columns: 1fr;
  }

  .layout-selector {
    padding: 1rem;
  }
}
</style>

