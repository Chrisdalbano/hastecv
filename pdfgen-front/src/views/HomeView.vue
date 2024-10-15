<template>
  <div class="container">
    <div class="form-preview-wrapper">
      <!-- Form Section -->
      <div
        :class="[
          'form-section',
          { 'hidden-mobile': isPreviewVisible && isMobile }
        ]"
      >
        <div class="form-header">
          <div class="switch-toggle">
            <AppLink
              to="/app"
              class="toggle-link"
              :class="{ active: currentRoute === '/app' }"
            >
              MANUAL
            </AppLink>
            <AppLink
              to="/app/json"
              class="toggle-link"
              :class="{ active: currentRoute === '/app/json' }"
            >
              JSON
            </AppLink>
          </div>
          <div class="template-selector-wrapper">
            <label class="template-label">Style:</label>
            <TemplateSelector @select="updateTemplate" />
          </div>
          <div class="sub-options">
            <button @click="injectDummyData" class="option-button">
              Load Test Data
            </button>
            <div class="divider"></div>
            <button @click="clearData" class="option-button">Clear Data</button>
          </div>
        </div>

        <!-- Render the form -->
        <router-view v-slot="{ Component, route }">
          <Transition mode="out-in" name="fade">
            <component :is="Component" :key="route.path" />
          </Transition>
        </router-view>
      </div>

      <!-- CV Preview Section -->
      <div
        :class="[
          'preview-section',
          { 'hidden-mobile': !isPreviewVisible && isMobile }
        ]"
      >
        <PreviewCV :downloadLink="store.downloadLink" />
      </div>
    </div>

    <!-- Generate Button and Overlay -->
    <div class="generate-button-overlay">
      <div class="button-group">
        <GenerateButton />
        <button v-if="isMobile" @click="togglePreview" class="haste-button">
          {{ isPreviewVisible ? "BACK" : "VISUALIZE" }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import TemplateSelector from "@/components/home/TemplateSelector.vue";
import PreviewCV from "@/components/home/PreviewCV.vue";
import AppLink from "@/components/AppLink.vue";
import GenerateButton from "@/components/GenerateButton.vue";
import { useResumeDataStore } from "../stores/resumeData";
import { ref, onMounted, onUnmounted, watch } from "vue";
import { useRoute } from "vue-router";

const store = useResumeDataStore();
const isMobile = ref(window.innerWidth <= 768);
const isPreviewVisible = ref(false);
const route = useRoute();
const currentRoute = ref(route.path);

// Update currentRoute whenever the route changes
watch(route, (newRoute) => {
  currentRoute.value = newRoute.path;
});

// Update window size status
function checkWindowSize() {
  isMobile.value = window.innerWidth <= 768;
}

onMounted(() => {
  window.addEventListener("resize", checkWindowSize);
  checkWindowSize();
});
onUnmounted(() => {
  window.removeEventListener("resize", checkWindowSize);
});

// Template update handler
function updateTemplate(newTemplate) {
  store.template = newTemplate;
}

// Inject dummy data into the store
function injectDummyData() {
  store.resumeData = {
    name: "John Doe",
    title: "Software Engineer",
    contact: {
      email: "john.doe@example.com",
      phone: "123-456-7890",
      location: "New York, USA",
      linkedin: "https://linkedin.com/in/johndoe",
      github: "https://github.com/johndoe",
      website: "https://johndoe.dev"
    },
    summary: [
      "Highly skilled Software Engineer with 5+ years of experience in building scalable web applications and services.",
      "Proficient in JavaScript, Vue.js, Python, and various backend technologies."
    ],
    experience: [
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
    ],
    education: [
      {
        degree: "Bachelor of Science in Computer Science",
        institution: "University of Technology",
        dates: "2013 - 2017"
      }
    ],
    skills: [
      "JavaScript",
      "Vue.js",
      "Node.js",
      "Python",
      "Django",
      "REST APIs",
      "SQL/NoSQL Databases"
    ]
  };
}

// Clear resume data in the store
function clearData() {
  store.clearResumeData();
}

// Toggle preview visibility
function togglePreview() {
  isPreviewVisible.value = !isPreviewVisible.value;
}
</script>

<script>
export default {
  useHead: {
    title: "HasteCV - Create ATS Beating Resumes",
    meta: [
      {
        name: "description",
        content:
          "Create professional, ATS-compliant resumes effortlessly with HasteCV. Use manual or JSON modes for ultimate control."
      },
      {
        name: "keywords",
        content:
          "resume builder, ATS resume, job application, CV builder, resume templates"
      },
      { property: "og:title", content: "HasteCV - Create ATS Beating Resumes" },
      {
        property: "og:description",
        content:
          "Easily build ATS-compliant resumes in minutes using HasteCV. Manual and JSON editing available."
      }
    ]
  }
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  max-width: 100vw;
  height: 100vh;
  overflow: hidden;
  position: relative;
  padding: 1rem;
}

.form-preview-wrapper {
  display: flex;
  height: calc(100% - 100px);
  gap: 1.5rem;
}

.form-section,
.preview-section {
  flex: 1;
  overflow-y: auto;
  padding: 1.5rem;
  background: rgba(20, 20, 20, 0.85);
  border-radius: 2px;
  scrollbar-color: rgba(255, 69, 0, 0.5) transparent;
  -ms-overflow-style: none;
  scrollbar-width: none;
}

.form-section::-webkit-scrollbar,
.preview-section::-webkit-scrollbar {
  display: none;
}

.hidden-mobile {
  display: none;
}

.generate-button-overlay {
  position: fixed;
  bottom: 60px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  background: rgba(0, 0, 0, 0.9);
  z-index: 30;
  border-radius: 2px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
}

.button-group {
  display: flex;
  gap: 10px;
}

.button-group button {
  font-size: 1.3rem;
}

.form-header {
  gap: 1rem;
}

.toggle-preview-button {
  font-size: 1rem;
  padding: 0.5rem 1.2rem;
  background: transparent;
  color: #ff4500;
  border: 2px solid #ff4500;
  border-radius: 2px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.toggle-preview-button:hover {
  background: #ff4500;
  color: #fff;
}

@media (max-width: 768px) {
  .form-preview-wrapper {
    flex-direction: column;
    height: calc(100% - 150px);
  }

  .form-section,
  .preview-section {
    flex: 1;
  }

  .form-header {
    flex-direction: column;
    gap: 1rem;
  }

  .switch-toggle {
    justify-content: center;
    width: 100%;
  }

  .template-selector-wrapper,
  .sub-options {
    justify-content: center;
    width: 100%;
  }
}

.form-header {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 2px solid var(--haste-yellow);
  background: rgba(20, 20, 20, 0.9);
  border-radius: 2px;
  margin-bottom: 1rem;
}

.switch-toggle {
  display: flex;
  gap: 10px;
  flex: 1;
}

.toggle-link {
  padding: 10px 20px;
  border: 2px solid var(--haste-yellow);
  border-radius: 2px;
  color: var(--haste-yellow);
  text-align: center;
  text-decoration: none;
  font-weight: 600;
  transition:
    background-color 0.3s ease,
    color 0.3s ease;
  cursor: pointer;
}

.toggle-link.active {
  background-color: var(--haste-yellow);
  color: #000;
}

.toggle-link:hover {
  background-color: var(--haste-yellow);
  color: #000;
}

.template-selector-wrapper {
  display: flex;
  align-items: center;
  gap: 10px;
}

.template-label {
  font-size: 1rem;
  color: var(--haste-yellow);
  font-weight: bold;
}

.sub-options {
  display: flex;
  align-items: center;
  gap: 10px;
}

.option-button {
  background: transparent;
  color: var(--haste-yellow);
  border: 2px solid var(--haste-yellow);
  padding: 5px 15px;
  border-radius: 2px;
  font-weight: 600;
  cursor: pointer;
  transition:
    background-color 0.3s ease,
    color 0.3s ease;
}

.option-button:hover {
  background-color: var(--haste-yellow);
  color: #000;
}

.divider {
  width: 1px;
  height: 20px;
  background-color: var(--haste-yellow);
}
</style>
