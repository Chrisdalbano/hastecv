<template>
  <section class="preview-container">
    <div class="preview-card">
      <iframe
        v-if="props.downloadLink"
        :src="props.downloadLink"
        class="cv-preview"
        title="CV Preview"
        scrolling="yes"
      ></iframe>
      <p v-else class="preview-placeholder">PREVIEW OF CV WILL BE SHOWN HERE</p>
    </div>

    <div class="mt-6 flex justify-center">
      <DownloadLink
        v-if="props.downloadLink"
        :downloadLink="store.downloadLink"
      ></DownloadLink>
    </div>
  </section>
</template>

<script setup>
import { useResumeDataStore } from "../../stores/resumeData";
import DownloadLink from "../DownloadLink.vue";

const props = defineProps({
  downloadLink: {
    required: true
  }
});

const store = useResumeDataStore();
</script>

<style scoped>
/* Overall container */
.preview-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 1.5rem;
  width: 100%;
}

/* Card style for the CV preview */
.preview-card {
  position: relative;
  width: 100%;
  max-width: 800px; /* You can remove this if you want full width */
  height: 70vh; /* Maintain height */
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow:
    5px 5px 20px rgba(0, 0, 0, 0.15),
    -5px -5px 20px rgba(255, 109, 12, 0.1);
  overflow: hidden;
  background-color: rgba(20, 20, 20, 0.85);
  margin-bottom: 1rem;
}

/* CV Preview (iframe) */
.cv-preview {
  width: 100%;
  height: 100%; /* Fill the parent */
  border: none;
  border-radius: 8px;
  box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
}

/* Placeholder when no preview is available */
.preview-placeholder {
  font-size: 1.3rem;
  color: var(--haste-yellow);
  font-weight: bold;
  text-align: center;
  padding: 2rem;
  z-index: 1;
  opacity: 0.9;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .preview-card {
    width: 95%;
    height: 60vh; /* Adjust for smaller screens */
    margin-top: 1rem;
  }

  .preview-placeholder {
    font-size: 1.1rem;
    padding: 1rem;
  }
}
</style>
