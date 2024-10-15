<template>
  <section class="preview-container">
    <!-- CV Preview Overlay with Glassmorphism Effect -->
    <div class="preview-card">
      <div class="">
        <!-- Blob Animation -->
        <div class="blob"></div>
        <!-- Display the CV Preview -->
        <iframe
          v-if="props.downloadLink"
          :src="props.downloadLink"
          class="cv-preview"
          title="CV Preview"
        ></iframe>
        <p v-else class="preview-placeholder">
          PREVIEW OF CV WILL BE SHOWN HERE
        </p>
      </div>
    </div>

    <!-- Download Link -->
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
  max-width: 800px;
  height: 70vh;
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

/* Glass effect */
.glass-effect {
  position: absolute;
  top: 5px;
  left: 5px;
  width: calc(100% - 10px);
  height: calc(100% - 10px);
  border-radius: 12px;
  background: rgba(19, 19, 19, 0.1);
  backdrop-filter: blur(10px);
  border: 2px solid rgba(255, 17, 0, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
}

/* Blob animation */
.blob {
  position: absolute;
  z-index: 0;
  top: 50%;
  left: 50%;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background-color: var(--haste-yellow);
  opacity: 0.15;
  filter: blur(20px);
  animation: blob-bounce 6s infinite ease-in-out;
}

@keyframes blob-bounce {
  0%,
  100% {
    transform: translate(-50%, -50%) translate3d(0, 0, 0);
  }
  25% {
    transform: translate(-50%, -50%) translate3d(15%, 0, 0);
  }
  50% {
    transform: translate(-50%, -50%) translate3d(15%, 15%, 0);
  }
  75% {
    transform: translate(-50%, -50%) translate3d(0, 15%, 0);
  }
}

/* CV Preview (iframe) */
.cv-preview {
  position: relative;
  z-index: 1;
  width: 100%;
  height: 100%;
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

/* Button container styling */
.button-container {
  display: flex;
  flex-direction: row;
  gap: 1rem;
  margin-top: 1rem;
  justify-content: center;
}

/* Action Buttons */
.action-button {
  background-color: rgba(255, 17, 0, 0.8);
  color: #fff;
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
  box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
}

.action-button:hover {
  background-color: rgba(255, 17, 0, 1);
}

.generate-button {
  background-color: rgba(0, 128, 255, 0.8);
}

.generate-button:hover {
  background-color: rgba(0, 128, 255, 1);
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .preview-card {
    width: 95%;
    height: 40vh;
    margin-top: 1rem;
  }

 

  .blob {
    width: 200px;
    height: 200px;
    filter: blur(15px);
  }

  .preview-placeholder {
    font-size: 1.1rem;
    padding: 1rem;
  }

  .button-container {
    flex-direction: column;
    gap: 0.5rem;
  }

  .action-button {
    width: 100%;
    padding: 0.7rem;
  }
}
</style>
