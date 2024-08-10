<template>
  <div class="preview-overlay">
    <iframe
      v-if="props.downloadLink"
      :src="props.downloadLink"
      class="h-full w-full border"
    ></iframe>
    <div v-else class="preview-placeholder">
      Preview of your CV will appear here
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  downloadLink: {
    required: true
  }
});
</script>

<style scoped>
.preview-overlay {
  flex: 1;
  position: relative;
  margin: 2rem;
  height: 90%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #1414147c;
}

.preview-placeholder {
  color: var(--haste-yellow);

  font-size: 30px;
  font-family: "OpenSans";
  text-align: center;
}
</style>
