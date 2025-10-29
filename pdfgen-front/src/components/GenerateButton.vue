<template>
  <button
    @click="handleGenerate"
    :disabled="!canGenerate || isGenerating"
    class="generate-button"
  >
    <span v-if="!isGenerating">GENERATE RESUME</span>
    <span v-else class="generating">
      <span class="spinner"></span>
      Generating...
    </span>
  </button>
</template>

<script setup>
import { useResumeDataStore } from "@/stores/resumeData";
import { useThemeStore } from "@/stores/themeStore";
import { useRoute } from "vue-router";
import { ref, watch } from "vue";
import { useCanvasStore } from "@/stores/canvasStore";

// Props
const props = defineProps({
  customizationPanel: {
    type: Object,
    default: null
  }
});

const store = useResumeDataStore();
const themeStore = useThemeStore();
const canvasStore = useCanvasStore();
const route = useRoute();
const canGenerate = ref(store.consentAccepted);
const isGenerating = ref(false);

// Expose generate method for parent components
defineExpose({
  handleGenerate,
  isGenerating
});

// Watching for changes in consent status
watch(
  () => store.consentAccepted,
  (newVal) => {
    canGenerate.value = newVal;
  }
);

async function handleGenerate() {
  console.log('Generate button clicked');
  
  if (!canGenerate.value) {
    alert("You need to accept cookies to generate a resume.");
    return;
  }

  isGenerating.value = true;
  console.log('Starting generation...');

  try {
    // Get layout settings from customization panel
    const layoutSettings = props.customizationPanel?.getLayoutSettings?.() || {};
    console.log('Layout settings:', layoutSettings);
    
    // Check if we're in visual builder mode
    if (route.path === '/app/visual') {
      console.log('Visual builder mode');
      // Visual builder generation
      if (canvasStore.enabledSections.length === 0) {
        alert('Please enable at least one section');
        isGenerating.value = false;
        return;
      }

      const layout = canvasStore.generateLayout();
      const apiUrl = import.meta.env.VITE_API_URL || 'http://127.0.0.1:5000';
      
      console.log('Sending request to:', `${apiUrl}/generate-visual`);
      console.log('Layout:', layout);
      
      const response = await fetch(`${apiUrl}/generate-visual`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          layout: layout,
          data: store.resumeData,
          filename: store.filename || 'resume',
          theme_color: themeStore.getPDFColor(),
          language: store.language,
          layout_type: layoutSettings.layout,
          spacing: layoutSettings.spacing,
          alignment: layoutSettings.alignment,
          margins: layoutSettings.margin
        })
      });

      console.log('Response status:', response.status);

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error || 'Failed to generate PDF');
      }

      const blob = await response.blob();
      console.log('Blob received, size:', blob.size);
      store.downloadLink = URL.createObjectURL(blob);
      console.log('Download link created:', store.downloadLink);
    } else {
      // Regular generation (Manual/JSON mode)
      console.log('Regular mode (Manual/JSON)');
      console.log('Resume data:', store.resumeData);
      console.log('Theme color:', themeStore.getPDFColor());
      console.log('Layout settings:', layoutSettings);
      await store.generatePdf(JSON.stringify(store.resumeData), {
        theme_color: themeStore.getPDFColor(),
        layout_type: layoutSettings.layout,
        spacing: layoutSettings.spacing,
        alignment: layoutSettings.alignment,
        margins: layoutSettings.margin
      });
      console.log('PDF generated, download link:', store.downloadLink);
    }
  } catch (error) {
    console.error('Error generating PDF:', error);
    alert(`Failed to generate PDF: ${error.message}`);
  } finally {
    isGenerating.value = false;
    console.log('Generation complete');
  }
}
</script>

<style scoped>
.generate-button {
  padding: 1rem 3rem;
  background: var(--haste-primary);
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: 700;
  font-size: 1.125rem;
  cursor: pointer;
  transition: all 0.2s;
  letter-spacing: 0.5px;
  text-transform: uppercase;
  box-shadow: 0 4px 12px rgba(var(--haste-primary-rgb), 0.3);
}

.generate-button:hover:not(:disabled) {
  background: var(--haste-primary);
  filter: brightness(1.1);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(var(--haste-primary-rgb), 0.4);
}

.generate-button:active:not(:disabled) {
  transform: translateY(0);
}

.generate-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

.generating {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.spinner {
  width: 16px;
  height: 16px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.6s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
