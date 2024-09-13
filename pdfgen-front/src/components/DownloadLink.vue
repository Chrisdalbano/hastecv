<template>
  <a
    :href="props.downloadLink"
    download="resume.pdf"
    class="haste-button"
  >
    Download Resume
  </a>
</template>

<script setup>
const props = defineProps({
  downloadLink: {
    required: true,
    type: String
  }
});
</script>

<style scoped></style>
