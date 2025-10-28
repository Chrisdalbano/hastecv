import { defineStore } from "pinia";
import { ref, watch, onMounted } from "vue";
import { useCookies } from "vue3-cookies";

// Get the backend URL from the environment variable
const apiUrl = import.meta.env.VITE_API_URL || "http://127.0.0.1:5000"; // Fallback to localhost if not set

// Language field labels
export const LANGUAGE_LABELS = {
  en: {
    'Personal Information': 'Personal Information',
    name: "Full Name",
    title: "Job Title",
    email: "Email",
    phone: "Phone",
    location: "Location",
    website: "Website",
    summary: "Professional Summary",
    experience: "Work Experience",
    education: "Education",
    skills: "Skills",
    position: "Position",
    company: "Company",
    dates: "Dates",
    degree: "Degree",
    institution: "Institution",
    responsibilities: "Responsibilities",
    technologies: "Technologies",
    Add: "Add",
    Skill: "Skill",
    'No work experience added yet': "No work experience added yet",
    'No education added yet': "No education added yet",
    'No skills added yet': "No skills added yet",
  },
  es: {
    'Personal Information': 'Información Personal',
    name: "Nombre Completo",
    title: "Puesto de Trabajo",
    email: "Correo",
    phone: "Teléfono",
    location: "Ubicación",
    website: "Sitio Web",
    summary: "Resumen Profesional",
    experience: "Experiencia Laboral",
    education: "Educación",
    skills: "Habilidades",
    position: "Puesto",
    company: "Empresa",
    dates: "Fechas",
    degree: "Título",
    institution: "Institución",
    responsibilities: "Responsabilidades",
    technologies: "Tecnologías",
    Add: "Añadir",
    Skill: "Habilidad",
    'No work experience added yet': "Sin experiencia laboral añadida",
    'No education added yet': "Sin educación añadida",
    'No skills added yet': "Sin habilidades añadidas",
  },
  fr: {
    'Personal Information': 'Informations Personnelles',
    name: "Nom Complet",
    title: "Titre du Poste",
    email: "Email",
    phone: "Téléphone",
    location: "Localisation",
    website: "Site Web",
    summary: "Résumé Professionnel",
    experience: "Expérience Professionnelle",
    education: "Éducation",
    skills: "Compétences",
    position: "Poste",
    company: "Entreprise",
    dates: "Dates",
    degree: "Diplôme",
    institution: "Institution",
    responsibilities: "Responsabilités",
    technologies: "Technologies",
    Add: "Ajouter",
    Skill: "Compétence",
    'No work experience added yet': "Aucune expérience professionnelle ajoutée",
    'No education added yet': "Aucune éducation ajoutée",
    'No skills added yet': "Aucune compétence ajoutée",
  },
  de: {
    'Personal Information': 'Persönliche Informationen',
    name: "Vollständiger Name",
    title: "Berufsbezeichnung",
    email: "Email",
    phone: "Telefon",
    location: "Standort",
    website: "Website",
    summary: "Berufliche Zusammenfassung",
    experience: "Berufserfahrung",
    education: "Ausbildung",
    skills: "Fähigkeiten",
    position: "Position",
    company: "Unternehmen",
    dates: "Daten",
    degree: "Abschluss",
    institution: "Institution",
    responsibilities: "Verantwortungen",
    technologies: "Technologien",
    Add: "Hinzufügen",
    Skill: "Fähigkeit",
    'No work experience added yet': "Keine Berufserfahrung hinzugefügt",
    'No education added yet': "Keine Ausbildung hinzugefügt",
    'No skills added yet': "Keine Fähigkeiten hinzugefügt",
  },
  pt: {
    'Personal Information': 'Informações Pessoais',
    name: "Nome Completo",
    title: "Cargo",
    email: "Email",
    phone: "Telefone",
    location: "Localização",
    website: "Site",
    summary: "Resumo Profissional",
    experience: "Experiência Profissional",
    education: "Educação",
    skills: "Habilidades",
    position: "Cargo",
    company: "Empresa",
    dates: "Datas",
    degree: "Diploma",
    institution: "Instituição",
    responsibilities: "Responsabilidades",
    technologies: "Tecnologias",
    Add: "Adicionar",
    Skill: "Habilidade",
    'No work experience added yet': "Sem experiência profissional adicionada",
    'No education added yet': "Sem educação adicionada",
    'No skills added yet': "Sem habilidades adicionadas",
  },
};

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
  const template = ref("executive");
  const filename = ref("resume");  // Custom filename (without .pdf extension)
  const consentAccepted = ref(cookies.get("consentAccepted") === "true");
  const language = ref(cookies.get("language") || "en");

  // Load saved data from localStorage (if available) on app start
  onMounted(() => {
    const savedResumeData = localStorage.getItem("resumeData");
    if (savedResumeData) {
      try {
        const parsedData = JSON.parse(savedResumeData);
        
        // Validate and sanitize loaded data to ensure arrays exist
        resumeData.value = {
          name: parsedData.name || "",
          title: parsedData.title || "",
          contact: {
            email: parsedData.contact?.email || "",
            phone: parsedData.contact?.phone || "",
            location: parsedData.contact?.location || "",
            website: parsedData.contact?.website || ""
          },
          summary: parsedData.summary || "",
          experience: Array.isArray(parsedData.experience) ? parsedData.experience : [],
          education: Array.isArray(parsedData.education) ? parsedData.education : [],
          skills: Array.isArray(parsedData.skills) ? parsedData.skills : []
        };
      } catch (error) {
        console.error("Error loading resume data from localStorage:", error);
        // If parsing fails, keep the default initialized data
      }
    }
    
    const savedLanguage = localStorage.getItem("language");
    if (savedLanguage) {
      language.value = savedLanguage;
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

  // Watch for language changes and persist
  watch(language, (newLang) => {
    localStorage.setItem("language", newLang);
    cookies.set("language", newLang, "365d");
  });

  // Watch for changes in consent and update the cookies accordingly
  watch(consentAccepted, (newVal) => {
    cookies.set("consentAccepted", newVal, "7d");
  });

  function updateConsentStatus(status) {
    consentAccepted.value = status;
  }

  function setLanguage(lang) {
    language.value = lang;
  }

  function getLabel(key) {
    return LANGUAGE_LABELS[language.value]?.[key] || LANGUAGE_LABELS.en[key] || key;
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
        `${apiUrl}/generate`, // Use dynamic API URL
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ 
            data: jsonData, 
            template: template.value,
            language: language.value  // Send language to backend
          })
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
    filename,
    consentAccepted,
    updateConsentStatus,
    clearResumeData,
    language,
    setLanguage,
    getLabel,
    LANGUAGE_LABELS,
  };
});
