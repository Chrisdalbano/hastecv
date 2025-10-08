<template>
  <a
    :href="props.downloadLink"
    :download="downloadFilename"
    class="haste-button"
  >
    Download Resume
  </a>
</template>

<script setup>
import { computed } from 'vue';
import { useResumeDataStore } from "../stores/resumeData";

const props = defineProps({
  downloadLink: {
    required: true,
    type: String
  }
});

const store = useResumeDataStore();

const downloadFilename = computed(() => {
  const filename = store.filename || 'resume';
  return `${filename}.pdf`;
});
</script>

<style scoped></style>
