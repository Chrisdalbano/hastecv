<template>
  <div class="preview-container">
    <!-- PDF Viewer -->
    <div v-if="props.downloadLink" class="pdf-viewer">
      <!-- Controls -->
      <div class="pdf-controls">
        <div class="control-group">
          <span class="page-info">PDF Preview</span>
        </div>

        <div class="control-group">
          <DownloadLink :downloadLink="props.downloadLink" />
        </div>
      </div>

      <!-- PDF Display with Iframe -->
      <div class="pdf-display">
        <iframe
          :src="props.downloadLink + '#toolbar=1&navpanes=0&scrollbar=1'"
          class="pdf-iframe"
          title="PDF Preview"
        ></iframe>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="empty-state">
      <div class="empty-icon">📄</div>
      <h3>No Preview Yet</h3>
      <p>Generate your resume to see a preview here</p>
      <p class="hint">Fill in your information and click "Generate Resume"</p>
    </div>
  </div>
</template>

<script setup>
import DownloadLink from "../DownloadLink.vue";

const props = defineProps({
  downloadLink: {
    required: true
  }
});
</script>

<style scoped>
.preview-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: var(--gray-800);
  border-radius: 8px;
  overflow: hidden;
}

/* PDF Viewer */
.pdf-viewer {
  display: flex;
  flex-direction: column;
  height: 100%;
}

/* PDF Controls */
.pdf-controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: var(--gray-900);
  border-bottom: 1px solid var(--border-color);
  flex-shrink: 0;
}

.control-group {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.page-info {
  color: white;
  font-size: 0.875rem;
  font-weight: 500;
}

/* PDF Display Container */
.pdf-display {
  flex: 1;
  overflow: hidden;
  background: var(--gray-700);
  padding: 0;
  min-height: 0;
}

/* PDF Iframe */
.pdf-iframe {
  width: 100%;
  height: 100%;
  border: none;
  background: white;
}

/* Empty State */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  text-align: center;
  padding: 3rem 2rem;
}

.empty-icon {
  font-size: 4rem;
  margin-bottom: 1.5rem;
  opacity: 0.3;
}

.empty-state h3 {
  margin: 0 0 0.75rem 0;
  font-size: 1.5rem;
  color: white;
  font-weight: 600;
}

.empty-state p {
  margin: 0.5rem 0;
  font-size: 1rem;
  color: var(--gray-400);
}

.hint {
  font-size: 0.875rem !important;
  color: var(--gray-500) !important;
  font-style: italic;
}
</style>
