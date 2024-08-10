<template>
  <a
    :href="props.downloadLink"
    download="resume.pdf"
    class="rounded bg-green-500 p-2 text-white"
  >
    Download PDF
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
