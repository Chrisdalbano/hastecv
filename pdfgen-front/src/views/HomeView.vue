<template>
  <div
    style="--min-width: 300"
    class="center relative z-10 grid grid-cols-2 gap-4 overflow-hidden p-1 py-4 max-lg:grid-cols-1"
  >
    <div class="space-y-4">
      <div class="flex flex-wrap items-center justify-center md:justify-between">
        <!-- Switch between Manual and JSON mode -->
        <div class="switch-toggle">
          <AppLink to="/app" class="flex-1">Manual</AppLink>
          <AppLink to="/app/json" class="flex-1">JSON</AppLink>
        </div>
        <div class="mx-2 flex items-center">
          <label class="text-xl font-bold text-haste-yellow">STYLE:</label>
          <TemplateSelector @select="updateTemplate" />
        </div>
      </div>

      <!-- Button to inject dummy data -->
      <button @click="injectDummyData" class="text-[var(--haste-yellow)]">Load Test Data</button>

      <!-- Dynamic rendering of the selected view -->
      <router-view v-slot="{ Component, route }">
        <Transition mode="out-in" name="fade">
          <component :is="Component" :key="route.path" />
        </Transition>
      </router-view>
    </div>

    <!-- CV Preview Component -->
    <PreviewCV class="min-w-[--min-width]" :downloadLink="store.downloadLink" />
  </div>
</template>

<script setup>
import TemplateSelector from "@/components/home/TemplateSelector.vue";
import PreviewCV from "@/components/home/PreviewCV.vue";
import AppLink from "@/components/AppLink.vue"; // AppLink for routing
import { useResumeDataStore } from "../stores/resumeData";

// Use the Pinia store
const store = useResumeDataStore();

// Function to update the selected template
function updateTemplate(newTemplate) {
  store.template = newTemplate;
}

// Function to inject dummy data into the store for testing
function injectDummyData() {
  store.resumeData.name = "John Doe";
  store.resumeData.title = "Software Engineer";
  store.resumeData.contact.email = "john.doe@example.com";
  store.resumeData.contact.phone = "123-456-7890";
  store.resumeData.contact.location = "New York, USA";
  store.resumeData.contact.linkedin = "https://linkedin.com/in/johndoe";
  store.resumeData.contact.github = "https://github.com/johndoe";
  store.resumeData.contact.website = "https://johndoe.dev";
  
  store.resumeData.summary = [
    "Highly skilled Software Engineer with 5+ years of experience in building scalable web applications and services.",
    "Proficient in JavaScript, Vue.js, Python, and various backend technologies."
  ];

  store.resumeData.experience = [
    {
      position: "Lead Software Engineer",
      company: "TechCorp Solutions",
      dates: "Jan 2020 - Present",
      responsibilities: [
        "Led a team of 10 engineers to build scalable web platforms using Vue.js and Node.js.",
        "Architected a microservices backend that improved response time by 30%.",
        "Mentored junior developers and conducted code reviews."
      ]
    },
    {
      position: "Software Engineer",
      company: "Innovative Web Apps",
      dates: "Jun 2017 - Dec 2019",
      responsibilities: [
        "Developed and maintained web applications using Vue.js and Django.",
        "Collaborated with the UX/UI team to improve the user experience.",
        "Automated testing processes and improved deployment pipelines."
      ]
    }
  ];

  store.resumeData.education = [
    {
      degree: "Bachelor of Science in Computer Science",
      institution: "University of Technology",
      dates: "2013 - 2017"
    }
  ];

  store.resumeData.skills = [
    "JavaScript",
    "Vue.js",
    "Node.js",
    "Python",
    "Django",
    "REST APIs",
    "SQL/NoSQL Databases"
  ];
}
</script>

<style scoped>
.switch-toggle {
  --max-width: 260px;
  background: transparent;
  display: flex;
  max-width: var(--max-width);
}

.haste-button {
  font-size: 1.2rem;
  padding: 0.75rem 1.5rem;
  background-color: transparent;
  color: var(--haste-yellow);
  border: 2px solid var(--haste-yellow);
  transition: all 0.3s ease;
  border-radius: 5px;
  margin-top: 1rem;
}

.haste-button:hover {
  background-color: var(--haste-yellow);
  color: var(--primary-black);
  transform: scale(1.05);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.25s ease-in-out;
}
</style>
