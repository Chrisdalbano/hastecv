<template>
  <a
    :href="props.downloadLink"
    :download="downloadFilename"
    class="download-button"
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

<style scoped>
.download-button {
  display: inline-block;
  padding: 0.625rem 1.25rem;
  background: transparent;
  color: var(--haste-primary);
  border: 2px solid var(--haste-primary);
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.875rem;
  text-decoration: none;
  transition: all 0.2s;
  text-align: center;
  white-space: nowrap;
}

.download-button:hover {
  background: var(--haste-primary);
  color: white;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(var(--haste-primary-rgb), 0.3);
}

.download-button:active {
  transform: translateY(0);
}
</style>
