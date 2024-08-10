<template>
  <div class="py-4 px-32 flex overflow-hidden relative">
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
            class="w-full h-full border"
          ></iframe>
          <div v-else class="preview-placeholder">
            Preview of your CV will appear here
          </div>
        </div>
      </div>
    </div>
    <div class="text-center p-4">
      <DownloadLink v-if="downloadLink" :downloadLink="downloadLink" />
    </div>
  </div>
</template>
<script>
import ResumeForm from "@/components/ResumeForm.vue";
import DownloadLink from "@/components/DownloadLink.vue";
import TemplateSelector from "@/components/TemplateSelector.vue";

export default {
  name: "App",
  components: {
    ResumeForm,
    DownloadLink,
    TemplateSelector,
  },
  data() {
    return {
      downloadLink: null,
      resumeData: {
        name: "",
        title: "",
        contact: {
          email: "",
          phone: "",
          location: "",
        },
      },
      template: "default",
    };
  },
  methods: {
    async generatePdf(jsonData) {
      try {
        const response = await fetch("http://127.0.0.1:5000/generate", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ data: jsonData, template: this.template }),
        });

        if (!response.ok) throw new Error("Failed to generate PDF");

        const blob = await response.blob();
        this.downloadLink = URL.createObjectURL(blob);
      } catch (error) {
        console.error("Error:", error);
      }
    },
    updateTemplate(template) {
      this.template = template;
    },
  },
};
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
