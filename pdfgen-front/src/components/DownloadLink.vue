<template>
  <div v-if="downloadLink" class="mt-4">
    <a
      :href="downloadLink"
      download="resume.pdf"
      class="rounded bg-green-500 p-2 text-white"
      >Download PDF</a
    >
  </div>
</template>

<script>
export default {
  name: "DownloadLink",
  props: {
    downloadLink: {
      type: String,
      required: true
    }
  }
};
</script>

<style scoped></style>
