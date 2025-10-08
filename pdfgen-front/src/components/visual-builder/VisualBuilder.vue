<template>
  <div class="visual-builder">
    <!-- Instructions Banner -->
    <div class="instructions-banner">
      <h3 class="instructions-title">Visual Layout Builder</h3>
      <p class="instructions-text">
        Control the order and visibility of sections in your resume. Check/uncheck to show/hide, reorder with arrows, then click Generate Resume at the bottom.
      </p>
    </div>

    <!-- Main Layout -->
    <div class="builder-layout">
      <!-- Sections Panel -->
      <div class="sections-panel">
        <div class="panel-header">
          <h3 class="panel-title">Resume Sections</h3>
          <button
            class="btn-add"
            @click="showAddMenu = !showAddMenu"
          >
            {{ showAddMenu ? '✕ Close' : '+ Add Section' }}
          </button>
        </div>

        <!-- Add Section Menu -->
        <transition name="slide-down">
          <div v-if="showAddMenu" class="add-section-menu">
            <button
              v-for="sectionType in availableSections"
              :key="sectionType.type"
              class="menu-item"
              @click="addSectionType(sectionType.type)"
            >
              {{ sectionType.label }}
            </button>
          </div>
        </transition>

        <!-- Sections List -->
        <div class="sections-list">
          <transition-group name="list" tag="div" class="sections-container">
            <div
              v-for="(section, index) in canvasStore.sections"
              :key="section.id"
              :class="['section-item', { 'section-disabled': !section.enabled }]"
            >
              <div class="section-row">
                <!-- Checkbox -->
                <label class="checkbox-container">
                  <input
                    type="checkbox"
                    :checked="section.enabled"
                    @change="canvasStore.toggleSection(section.id)"
                    class="checkbox-input"
                  />
                  <span class="checkbox-custom"></span>
                </label>

                <!-- Section Info -->
                <div class="section-info">
                  <span class="section-name">{{ formatSectionName(section.type) }}</span>
                  <span v-if="getSectionMeta(section.type)" class="section-meta">
                    {{ getSectionMeta(section.type) }}
                  </span>
                </div>

                <!-- Controls -->
                <div class="section-controls">
                  <button
                    class="control-btn"
                    :disabled="index === 0"
                    @click="canvasStore.moveUp(section.id)"
                    title="Move Up"
                  >
                    ↑
                  </button>
                  <button
                    class="control-btn"
                    :disabled="index === canvasStore.sections.length - 1"
                    @click="canvasStore.moveDown(section.id)"
                    title="Move Down"
                  >
                    ↓
                  </button>
                  <button
                    class="control-btn control-delete"
                    @click="canvasStore.removeSection(section.id)"
                    title="Remove"
                  >
                    ×
                  </button>
                </div>
              </div>

              <!-- Extra Properties for Spacer/Divider -->
              <div
                v-if="section.enabled && (section.type === 'spacer' || section.type === 'divider')"
                class="section-properties"
              >
                <div v-if="section.type === 'spacer'" class="property-group">
                  <label class="property-label">Height</label>
                  <select
                    :value="section.height"
                    @change="updateHeight(section.id, $event.target.value)"
                    class="property-select"
                  >
                    <option value="10px">10px</option>
                    <option value="20px">20px</option>
                    <option value="30px">30px</option>
                    <option value="50px">50px</option>
                  </select>
                </div>
                <div v-if="section.type === 'divider'" class="property-group">
                  <label class="property-label">Color</label>
                  <input
                    type="color"
                    :value="section.color"
                    @input="updateColor(section.id, $event.target.value)"
                    class="color-input"
                  />
                </div>
              </div>
            </div>
          </transition-group>

          <!-- Empty State -->
          <div v-if="canvasStore.sections.length === 0" class="empty-state">
            <p>No sections added yet.</p>
            <p>Click "+ Add Section" to get started.</p>
          </div>
        </div>

        <!-- Bottom Actions -->
        <div class="panel-footer">
          <button
            class="btn-reset"
            @click="canvasStore.resetSections()"
          >
            Reset to Default
          </button>
        </div>
      </div>

      <!-- Preview Panel -->
      <div class="preview-panel">
        <div class="preview-header">
          <h3 class="panel-title">Section Order Preview</h3>
          <p class="preview-subtitle">
            This shows what sections will appear and in what order
          </p>
        </div>
        <div class="preview-content">
          <transition-group name="preview-fade" tag="div" class="preview-list">
            <div
              v-for="(section, index) in canvasStore.enabledSections"
              :key="section.id"
              class="preview-item"
            >
              <div class="preview-number">{{ index + 1 }}</div>
              <div class="preview-details">
                <div class="preview-title">
                  {{ formatSectionName(section.type) }}
                </div>
                <div class="preview-description">
                  {{ getSectionPreview(section.type) }}
                </div>
              </div>
            </div>
          </transition-group>

          <!-- Empty State -->
          <div v-if="canvasStore.enabledSections.length === 0" class="empty-preview">
            <p>No sections enabled.</p>
            <p>Check some boxes to add sections to your resume.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCanvasStore } from '../../stores/canvasStore';
import { useResumeDataStore } from '../../stores/resumeData';

const canvasStore = useCanvasStore();
const resumeStore = useResumeDataStore();
const showAddMenu = ref(false);

const availableSections = [
  { type: 'header', label: 'Header' },
  { type: 'summary', label: 'Summary' },
  { type: 'experience', label: 'Experience' },
  { type: 'education', label: 'Education' },
  { type: 'skills', label: 'Skills' },
  { type: 'projects', label: 'Projects' },
  { type: 'technical_proficiency', label: 'Technical Proficiency' },
  { type: 'spacer', label: 'Spacer (Empty Space)' },
  { type: 'divider', label: 'Divider (Line)' }
];

function formatSectionName(type) {
  const names = {
    technical_proficiency: 'Technical Proficiency',
    spacer: 'Spacer',
    divider: 'Divider'
  };
  return names[type] || type.charAt(0).toUpperCase() + type.slice(1).replace(/_/g, ' ');
}

function getSectionMeta(type) {
  if (type === 'spacer') return 'Empty space';
  if (type === 'divider') return 'Horizontal line';
  return '';
}

function getSectionPreview(type) {
  const data = resumeStore.resumeData;

  switch (type) {
    case 'header':
      return data.name || 'Your name and contact information';
    case 'summary':
      return 'Professional summary paragraph';
    case 'experience':
      const expCount = data.experience?.length || 0;
      return `${expCount} work experience${expCount !== 1 ? 's' : ''}`;
    case 'education':
      const eduCount = data.education?.length || 0;
      return `${eduCount} education entr${eduCount !== 1 ? 'ies' : 'y'}`;
    case 'skills':
      const skillCount = data.skills?.length || 0;
      return `${skillCount} skill${skillCount !== 1 ? 's' : ''}`;
    case 'projects':
      const projCount = data.projects?.length || 0;
      return `${projCount} project${projCount !== 1 ? 's' : ''}`;
    case 'technical_proficiency':
      return 'Technical skills breakdown';
    case 'spacer':
      return 'Empty space for layout control';
    case 'divider':
      return 'Horizontal separator line';
    default:
      return '';
  }
}

function addSectionType(type) {
  canvasStore.addSection(type);
  showAddMenu.value = false;
}

function updateHeight(id, height) {
  canvasStore.updateSection(id, { height });
}

function updateColor(id, color) {
  canvasStore.updateSection(id, { color });
}
</script>

<style scoped>
.visual-builder {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  height: 100%;
  padding: 0.5rem;
}

/* Instructions Banner */
.instructions-banner {
  background: var(--gray-800);
  border: 1px solid var(--border-color);
  padding: 1.5rem;
  border-radius: 8px;
  position: relative;
  overflow: hidden;
}

.instructions-banner::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--haste-gradient);
}

.instructions-title {
  margin: 0 0 0.75rem 0;
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--haste-primary);
}

.instructions-text {
  margin: 0;
  font-size: 0.95rem;
  color: var(--gray-300);
  line-height: 1.6;
}

/* Builder Layout */
.builder-layout {
  display: grid;
  grid-template-columns: 420px 1fr;
  gap: 1.5rem;
  flex: 1;
  overflow: hidden;
  min-height: 0;
}

/* Sections Panel */
.sections-panel {
  display: flex;
  flex-direction: column;
  background: var(--gray-900);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  overflow: hidden;
}

.panel-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.25rem;
  background: var(--gray-800);
  border-bottom: 1px solid var(--border-color);
}

.panel-title {
  margin: 0;
  color: white;
  font-size: 1.1rem;
  font-weight: 600;
}

.btn-add {
  padding: 0.5rem 1rem;
  background: transparent;
  color: var(--haste-primary);
  border: 1px solid var(--haste-primary);
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-add:hover {
  background: var(--haste-primary);
  color: white;
  transform: translateY(-1px);
}

/* Add Section Menu */
.add-section-menu {
  background: var(--gray-800);
  border-bottom: 1px solid var(--border-color);
  padding: 1rem;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.5rem;
}

.menu-item {
  padding: 0.75rem;
  background: var(--gray-700);
  color: white;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 500;
  transition: all 0.2s;
  text-align: left;
}

.menu-item:hover {
  background: var(--haste-primary);
  border-color: var(--haste-primary);
  transform: translateY(-1px);
}

/* Sections List */
.sections-list {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.sections-container {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.section-item {
  background: var(--gray-800);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  overflow: hidden;
  transition: all 0.2s;
}

.section-item:hover {
  border-color: var(--haste-primary);
  box-shadow: 0 0 0 1px var(--haste-primary);
}

.section-disabled {
  opacity: 0.5;
}

.section-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem;
}

/* Checkbox */
.checkbox-container {
  position: relative;
  cursor: pointer;
  flex-shrink: 0;
}

.checkbox-input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
}

.checkbox-custom {
  display: block;
  width: 20px;
  height: 20px;
  background: var(--gray-700);
  border: 2px solid var(--haste-primary);
  border-radius: 4px;
  transition: all 0.2s;
}

.checkbox-input:checked + .checkbox-custom {
  background: var(--haste-primary);
}

.checkbox-custom::after {
  content: '✓';
  position: absolute;
  display: none;
  color: white;
  font-weight: bold;
  font-size: 14px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.checkbox-input:checked + .checkbox-custom::after {
  display: block;
}

/* Section Info */
.section-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  min-width: 0;
}

.section-name {
  color: white;
  font-weight: 600;
  font-size: 0.9375rem;
}

.section-meta {
  color: var(--gray-400);
  font-size: 0.8125rem;
}

/* Section Controls */
.section-controls {
  display: flex;
  gap: 0.25rem;
  flex-shrink: 0;
}

.control-btn {
  width: 32px;
  height: 32px;
  background: var(--gray-700);
  border: 1px solid var(--border-color);
  color: var(--haste-primary);
  border-radius: 4px;
  cursor: pointer;
  font-size: 1.125rem;
  font-weight: bold;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.control-btn:hover:not(:disabled) {
  background: var(--haste-primary);
  color: white;
  border-color: var(--haste-primary);
}

.control-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.control-delete:hover:not(:disabled) {
  background: #dc2626;
  border-color: #dc2626;
}

/* Section Properties */
.section-properties {
  padding: 1rem;
  background: var(--gray-900);
  border-top: 1px solid var(--border-color);
  display: flex;
  gap: 1rem;
}

.property-group {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.property-label {
  color: var(--gray-400);
  font-size: 0.875rem;
  font-weight: 500;
}

.property-select {
  padding: 0.5rem;
  background: var(--gray-700);
  color: white;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  font-size: 0.875rem;
}

.color-input {
  width: 60px;
  height: 32px;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  background: var(--gray-700);
  cursor: pointer;
}

/* Panel Footer */
.panel-footer {
  padding: 1rem;
  border-top: 1px solid var(--border-color);
  background: var(--gray-800);
}

.btn-reset {
  width: 100%;
  padding: 0.75rem;
  background: transparent;
  color: var(--gray-400);
  border: 1px solid var(--gray-600);
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-reset:hover {
  background: var(--gray-700);
  color: white;
  border-color: var(--gray-500);
}

/* Preview Panel */
.preview-panel {
  display: flex;
  flex-direction: column;
  background: var(--gray-900);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  overflow: hidden;
}

.preview-header {
  padding: 1.25rem;
  background: var(--gray-800);
  border-bottom: 1px solid var(--border-color);
}

.preview-subtitle {
  margin: 0.5rem 0 0 0;
  color: var(--gray-400);
  font-size: 0.875rem;
}

.preview-content {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.preview-list {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.preview-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: var(--gray-800);
  border-left: 3px solid var(--haste-primary);
  border-radius: 4px;
  transition: all 0.2s;
}

.preview-item:hover {
  background: var(--gray-700);
  transform: translateX(4px);
}

.preview-number {
  width: 36px;
  height: 36px;
  background: var(--haste-primary);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 1.125rem;
  flex-shrink: 0;
}

.preview-details {
  flex: 1;
  min-width: 0;
}

.preview-title {
  color: white;
  font-weight: 600;
  font-size: 0.9375rem;
  margin-bottom: 0.25rem;
}

.preview-description {
  color: var(--gray-400);
  font-size: 0.8125rem;
}

/* Empty States */
.empty-state,
.empty-preview {
  padding: 3rem 1rem;
  text-align: center;
  color: var(--gray-400);
}

.empty-state p,
.empty-preview p {
  margin: 0.5rem 0;
  font-size: 0.9375rem;
}

/* Animations */
.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.3s ease;
}

.slide-down-enter-from,
.slide-down-leave-to {
  opacity: 0;
  max-height: 0;
  transform: translateY(-10px);
}

.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.3s ease;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}

.preview-fade-move,
.preview-fade-enter-active,
.preview-fade-leave-active {
  transition: all 0.3s ease;
}

.preview-fade-enter-from,
.preview-fade-leave-to {
  opacity: 0;
}

/* Scrollbar Styling */
.sections-list::-webkit-scrollbar,
.preview-content::-webkit-scrollbar {
  width: 8px;
}

.sections-list::-webkit-scrollbar-track,
.preview-content::-webkit-scrollbar-track {
  background: var(--gray-800);
}

.sections-list::-webkit-scrollbar-thumb,
.preview-content::-webkit-scrollbar-thumb {
  background: var(--haste-primary);
  border-radius: 4px;
}

.sections-list::-webkit-scrollbar-thumb:hover,
.preview-content::-webkit-scrollbar-thumb:hover {
  background: var(--haste-primary);
  filter: brightness(1.2);
}

/* Responsive */
@media (max-width: 1024px) {
  .builder-layout {
    grid-template-columns: 1fr;
  }

  .sections-panel {
    max-height: 60vh;
  }

  .add-section-menu {
    grid-template-columns: 1fr;
  }
}
</style>
