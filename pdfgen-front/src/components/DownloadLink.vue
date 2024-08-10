<template>
    <div v-if="downloadLink" class="mt-4">
      <a :href="downloadLink" download="resume.pdf" class="bg-green-500 text-white p-2 rounded">Download PDF</a>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DownloadLink',
    props: {
      downloadLink: {
        type: String,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  </style>
  