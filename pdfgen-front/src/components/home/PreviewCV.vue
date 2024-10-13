<template>
  <section class="preview-container">
    <!-- CV Preview Overlay with Glassmorphism Effect -->
    <div class="preview-card">
      <div class="glass-effect">
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
  min-width: 500px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1rem;
  margin-top: 2rem;
  background-color: bla;
}

/* Card style for the CV preview */
.preview-card {
  position: relative;
  width: 100%;
  height: 70vh;
  border-radius: 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow:
    10px 10px 30px rgba(0, 0, 0, 0.25),
    -10px -10px 30px rgba(255, 109, 12, 0.15);
  overflow: hidden;
  background-color: rgba(20, 20, 20, 0.8);
}

/* Glass effect */
.glass-effect {
  position: absolute;
  top: 5px;
  left: 5px;
  width: calc(100% - 10px);
  height: calc(100% - 10px);
  border-radius: 2px;
  background: rgba(19, 19, 19, 0.1);
  backdrop-filter: blur(12px);
  border: 2px solid rgba(255, 17, 0, 0.3);
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
  width: 700px;
  height: 700px;
  border-radius: 50%;
  background-color: var(--haste-yellow);
  opacity: 0.2;
  filter: blur(30px);
  animation: blob-bounce 5s infinite ease-in-out;
}

@keyframes blob-bounce {
  0%,
  100% {
    transform: translate(-50%, -50%) translate3d(0, 0, 0);
  }
  25% {
    transform: translate(-50%, -50%) translate3d(50%, 0, 0);
  }
  50% {
    transform: translate(-50%, -50%) translate3d(50%, 50%, 0);
  }
  75% {
    transform: translate(-50%, -50%) translate3d(0, 50%, 0);
  }
}

/* CV Preview (iframe) */
.cv-preview {
  position: relative;
  z-index: 1;
  width: 100%;
  height: 100%;
  border: none;
  border-radius: 2px;
}

/* Placeholder when no preview is available */
.preview-placeholder {
  font-size: 2rem;
  color: var(--haste-yellow);
  font-weight: bold;
  max-width: 200px;
  
  text-align: center;
  z-index: 1;
  opacity: 0.9;
}
</style>
