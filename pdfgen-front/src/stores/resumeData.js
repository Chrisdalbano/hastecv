import { defineStore } from "pinia";
import { ref } from "vue";

export const useResumeDataStore = defineStore("resume", () => {
  const resumeData = ref({
    name: "",
    title: "",
    contact: {
      email: "",
      phone: "",
      location: "",
      linkedin: "",
      github: "",
      website: ""
    },
    summary: [],
    experience: [],
    education: [],
    skills: []
  });

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

  return { resumeData, downloadLink, generatePdf, template };
});
