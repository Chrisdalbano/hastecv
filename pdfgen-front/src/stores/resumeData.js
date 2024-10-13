import { defineStore } from "pinia";
import { ref, watch, onMounted } from "vue";
import { useCookies } from "vue3-cookies";

export const useResumeDataStore = defineStore("resume", () => {
  const { cookies } = useCookies();

  // Initialize resume data, which we will persist
  const resumeData = ref({
    name: "",
    title: "",
    contact: { email: "", phone: "", location: "" },
    summary: "",
    experience: [],
    education: [],
    skills: []
  });

  const downloadLink = ref(null);
  const template = ref("default");
  const consentAccepted = ref(cookies.get("consentAccepted") === "true");

  // Load saved data from localStorage (if available) on app start
  onMounted(() => {
    const savedResumeData = localStorage.getItem("resumeData");
    if (savedResumeData) {
      resumeData.value = JSON.parse(savedResumeData);
    }
  });

  // Watch for changes in `resumeData` and persist them in localStorage
  watch(
    resumeData,
    (newData) => {
      localStorage.setItem("resumeData", JSON.stringify(newData));
    },
    { deep: true }
  );

  // Watch for changes in consent and update the cookies accordingly
  watch(consentAccepted, (newVal) => {
    cookies.set("consentAccepted", newVal, "7d");
  });

  function updateConsentStatus(status) {
    consentAccepted.value = status;
  }

  function clearResumeData() {
    localStorage.removeItem("resumeData");
    resumeData.value = {
      name: "",
      title: "",
      contact: { email: "", phone: "", location: "" },
      summary: "",
      experience: [],
      education: [],
      skills: []
    };
  }

  async function generatePdf(jsonData) {
    if (!consentAccepted.value) {
      console.warn("User has not accepted cookies.");
      return;
    }

    try {
      const response = await fetch(
        `https://limitless-ravine-64006-56ec8f2bdbdc.herokuapp.com/generate`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ data: jsonData, template: template.value })
        }
      );

      if (!response.ok) throw new Error("Failed to generate PDF");

      const blob = await response.blob();
      downloadLink.value = URL.createObjectURL(blob);
    } catch (error) {
      console.error("Error:", error);
    }
  }

  return {
    resumeData,
    downloadLink,
    generatePdf,
    template,
    consentAccepted,
    updateConsentStatus,
    clearResumeData
  };
});
