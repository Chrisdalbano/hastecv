<template>
  <div class="center relative z-10 grid grid-cols-2 gap-4 overflow-hidden py-4">
    <div>
      <!-- refactor -->
      <TemplateSelector @select="updateTemplate" />

      <ResumeForm @submit="generatePdf" />
    </div>
    <PreviewCV />
  </div>
  <DownloadLink v-if="downloadLink" :downloadLink="downloadLink" />
</template>
<script setup>
import ResumeForm from "@/components/home/ResumeForm.vue";
import DownloadLink from "@/components/DownloadLink.vue";
import TemplateSelector from "@/components/home/TemplateSelector.vue";
import PreviewCV from "@/components/home/PreviewCV.vue";

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
