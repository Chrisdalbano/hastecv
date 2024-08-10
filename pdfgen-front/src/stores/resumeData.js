import { defineStore } from "pinia";
import { ref } from 'vue';

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
      website: "",
    },
    summary: [],
    experience: [],
    education: [],
    skills: [],
  });

  return { resumeData };

});
