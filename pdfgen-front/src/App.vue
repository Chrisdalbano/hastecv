<template>
  <div
    class="min-h-screen py-4 px-10 flex flex-col justify-center overflow-hidden relative"
  >
    <Header/>
    <div class="background-animation"></div>
    <div class="container mx-auto p-6 relative z-10">
      <div class="grid grid-cols-2 gap-4">
        <div>
          <ResumeForm @submit="generatePdf" />
          <TemplateSelector @select="updateTemplate" />
        </div>
        <div class="preview-overlay">
          <iframe
            v-if="downloadLink"
            :src="downloadLink"
            class="w-full h-full border"
          ></iframe>
          <div v-else class="preview-placeholder text-yellow-300">
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
import Header from "./components/Header.vue";
import ResumeForm from "./components/ResumeForm.vue";
import DownloadLink from "./components/DownloadLink.vue";
import TemplateSelector from "./components/TemplateSelector.vue";

export default {
  name: "App",
  components: {
    Header,
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
        // Add more default fields as necessary
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

<style>
@import "./assets/tailwind.css";

.min-h-screen {
  min-height: 100vh;
}

.background-animation {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    110deg,
    rgb(14, 14, 14) 52.4%,
    rgba(255, 208, 0, 0.788) 138.8%
  );
  z-index: -1;
}

.preview-overlay {
  position: relative;
  margin: 2rem;
  height: 90%;
  width: 90%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #141414;
}

.preview-placeholder {
  color: #ffd700;
  font-size: 1.2rem;
  text-align: center;
}

.iframe {
  border: none;
}

div.jsoneditor-menu > a {
  display: none;
}

.jsoneditor-menu {
  background-color: black;
  border-bottom: 1px solid rgb(255, 230, 0);
}
</style>
