<template>
  <section>
    <div class="preview-overlay">
      <iframe
        v-if="props.downloadLink"
        :src="props.downloadLink"
        class="h-full w-full border"
      ></iframe>
      <p v-else class="preview-placeholder px-4">
        Preview of your CV will appear here
      </p>
    </div>
    <div class="flex justify-center">
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
.preview-overlay {
  flex: 1;
  position: relative;
  margin: 1rem;
  margin-top: 0;
  height: 70svh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #1414147c;
  border: 2px solid black;
}

@media (max-width: 1024px) {
  .preview-overlay {
    margin: 0;
  }
}

.preview-placeholder {
  color: var(--haste-yellow);

  font-size: 30px;
  font-family: "OpenSans";
  text-align: center;
}
</style>
