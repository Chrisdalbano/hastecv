<template>
  <div class="relative flex overflow-hidden px-32 py-4">
    <div class="container relative z-10">
      <div class="grid grid-cols-2 gap-4">
        <div>
          <TemplateSelector @select="updateTemplate" />

          <ResumeForm @submit="generatePdf" />
        </div>
        <div class="preview-overlay">
          <iframe
            v-if="downloadLink"
            :src="downloadLink"
            class="h-full w-full border"
          ></iframe>
          <div v-else class="preview-placeholder">
            Preview of your CV will appear here
          </div>
        </div>
      </div>
    </div>
    <div class="p-4 text-center">
      <DownloadLink v-if="downloadLink" :downloadLink="downloadLink" />
    </div>
  </div>
</template>
<script setup>
import ResumeForm from "@/components/ResumeForm.vue";
import DownloadLink from "@/components/DownloadLink.vue";
import TemplateSelector from "@/components/TemplateSelector.vue";

import { ref } from "vue";

const downloadLink = ref(null);
const template = ref("default");

async function generatePdf(jsonData) {
  try {
    const response = await fetch("http://127.0.0.1:5000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ data: jsonData, template: template.value })
    });

    if (!response.ok) throw new Error("Failed to generate PDF");

    const blob = await response.blob();
    downloadLink.value = URL.createObjectURL(blob);
  } catch (error) {
    console.error("Error:", error);
  }
}

function updateTemplate(newTemplate) {
  template.value = newTemplate;
}
</script>

<style scoped>
.preview-overlay {
  position: relative;
  margin: 2rem;
  height: 90%;
  width: 90%;
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
