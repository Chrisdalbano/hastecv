<template>
  <div class="home-container">
    <!-- Top Control Bar -->
    <div class="control-bar">
      <div class="control-bar-content">
        <!-- Mode Tabs -->
        <div class="mode-tabs">
          <button
            v-for="mode in modes"
            :key="mode.path"
            :class="['mode-tab', { active: currentRoute === mode.path }]"
            @click="navigateTo(mode.path)"
          >
            {{ mode.label }}
          </button>
        </div>

        <!-- Right Controls -->
        <div class="right-controls">
          <!-- Filename Input -->
          <div class="control-group">
            <label class="control-label">Filename</label>
            <input
              v-model="store.filename"
              type="text"
              placeholder="resume"
              maxlength="50"
              class="control-input"
            />
            <span class="file-extension">.pdf</span>
          </div>

          <!-- Template Selector -->
          <div class="control-group">
            <label class="control-label">Template</label>
            <select
              v-model="store.template"
              class="control-select"
            >
              <option
                v-for="template in templates"
                :key="template.value"
                :value="template.value"
              >
                {{ template.label }}
              </option>
            </select>
          </div>

          <!-- Theme Selector -->
         

          <!-- Action Buttons -->
          <button @click="injectDummyData" class="action-btn">
            Load Test Data
          </button>
          <button @click="clearData" class="action-btn action-btn-danger">
            Clear
          </button>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <!-- Editor Section -->
      <div
        :class="[
          'editor-section',
          { 'hidden-mobile': isPreviewVisible && isMobile }
        ]"
      >
        <router-view v-slot="{ Component, route }">
          <Transition mode="out-in" name="fade">
            <component :is="Component" :key="route.path" />
          </Transition>
        </router-view>
      </div>

      <!-- Preview Section -->
      <div
        :class="[
          'preview-section',
          { 'hidden-mobile': !isPreviewVisible && isMobile }
        ]"
      >
        <div class="preview-card">
          <div class="preview-header">
            <h3 class="preview-title">Resume Preview</h3>
          </div>
          <div class="preview-body">
            <PreviewCV :downloadLink="store.downloadLink" />
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Action Bar - Single Generate Button -->
    <div class="bottom-bar">
      <div class="bottom-bar-content">
        <button
          v-if="isMobile"
          class="mobile-toggle"
          @click="togglePreview"
        >
          {{ isPreviewVisible ? "← Back to Editor" : "Preview →" }}
        </button>
        <GenerateButton />
      </div>
    </div>
  </div>
</template>

<script setup>
import PreviewCV from "@/components/home/PreviewCV.vue";
import GenerateButton from "@/components/GenerateButton.vue";
import { useResumeDataStore } from "../stores/resumeData";
import { useThemeStore } from "../stores/themeStore";
import { ref, onMounted, onUnmounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";

const store = useResumeDataStore();
const themeStore = useThemeStore();
const route = useRoute();
const router = useRouter();

// Load theme on mount
onMounted(() => {
  themeStore.loadTheme();
  window.addEventListener("resize", checkWindowSize);
  checkWindowSize();
});

onUnmounted(() => {
  window.removeEventListener("resize", checkWindowSize);
});

const isMobile = ref(window.innerWidth <= 768);
const isPreviewVisible = ref(false);
const currentRoute = ref(route.path);

const modes = [
  { path: '/app', label: 'Manual' },
  { path: '/app/json', label: 'JSON' },
  { path: '/app/visual', label: 'Visual Builder' }
];

const templates = ref([
  { value: "executive", label: "Executive" },
  { value: "modern", label: "Modern" },
  { value: "minimal", label: "Minimal" },
  { value: "creative", label: "Creative" },
  { value: "default", label: "Default" }
]);

// Update currentRoute when route changes
watch(route, (newRoute) => {
  currentRoute.value = newRoute.path;
}, { immediate: true });

// Navigate to different modes
function navigateTo(path) {
  router.push(path);
}

// Update window size status
function checkWindowSize() {
  isMobile.value = window.innerWidth <= 768;
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
    technical_proficiency: {
      "Frontend": "React, TypeScript, Vue.js, HTML5, JavaScript (ES6+), CSS3, Tailwind CSS, SASS",
      "Backend": "Node.js, Java, Spring Boot, RESTful APIs, GraphQL",
      "Database": "PostgreSQL, MongoDB, Firebase, Supabase, NoSQL",
      "Cloud": "Microsoft Azure, GCP, Docker, Kubernetes, CI/CD pipelines",
      "Tools": "Git, GitHub, Jenkins, Figma, Adobe XD, Jira, Webpack, Gulp, Grunt"
    },
    experience: [
      {
        position: "Lead Software Engineer",
        company: "TechCorp Solutions",
        dates: "Jan 2020 - Present",
        location: "Remote - Orlando, FL",
        responsibilities: [
          "Led a team of 10 engineers to build scalable web platforms using Vue.js and Node.js.",
          "Architected a microservices backend that improved response time by 30%.",
          "Mentored junior developers and conducted code reviews.",
          "Implemented CI/CD pipelines reducing deployment time by 50%."
        ],
        technologies: "Vue.js, Node.js, Docker, AWS, PostgreSQL"
      },
      {
        position: "Software Engineer",
        company: "Innovative Web Apps",
        dates: "Jun 2017 - Dec 2019",
        location: "Miami, FL",
        responsibilities: [
          "Developed and maintained web applications using Vue.js and Django.",
          "Collaborated with the UX/UI team to improve the user experience.",
          "Automated testing processes and improved deployment pipelines.",
          "Built RESTful APIs serving 100K+ daily active users."
        ],
        technologies: "Vue.js, Python, Django, REST APIs"
      },
      {
        position: "Junior Frontend Developer",
        company: "StartUp Inc",
        dates: "Jan 2016 - May 2017",
        location: "Orlando, FL",
        responsibilities: [
          "Developed responsive web interfaces using React and TypeScript.",
          "Integrated front-end components with Java-based backend microservices.",
          "Collaborated with designers to implement pixel-perfect UI/UX designs."
        ],
        technologies: "React, TypeScript, Java, Spring Boot"
      }
    ],
    education: [
      {
        degree: "Bachelor of Science in Computer Science",
        institution: "University of Technology",
        dates: "2013 - 2017",
        location: "Orlando, FL"
      }
    ],
    skills: [
      "JavaScript",
      "Vue.js",
      "React",
      "Node.js",
      "Python",
      "Django",
      "REST APIs",
      "SQL/NoSQL Databases",
      "Docker",
      "Kubernetes",
      "CI/CD"
    ],
    projects: [
      {
        name: "E-Commerce Platform",
        description: "Scalable Vue.js front-end for a custom eCommerce platform optimizing performance for 100K+ users.",
        technologies: "Vue.js, Node.js, PostgreSQL",
        link: "https://github.com/johndoe/ecommerce"
      }
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

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: hidden;
}

/* Control Bar */
.control-bar {
  background: var(--gray-900);
  border-bottom: 1px solid var(--border-color);
  padding: 1rem 1.5rem;
  flex-shrink: 0;
}

.control-bar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
  max-width: 1920px;
  margin: 0 auto;
}

/* Mode Tabs */
.mode-tabs {
  display: flex;
  gap: 0.5rem;
  flex-shrink: 0;
}

.mode-tab {
  padding: 0.625rem 1.25rem;
  background: transparent;
  color: white;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.9375rem;
  cursor: pointer;
  transition: all 0.2s;
}

.mode-tab:hover {
  background: var(--hover-color);
  border-color: var(--haste-primary);
}

.mode-tab.active {
  background: var(--haste-primary);
  border-color: var(--haste-primary);
  color: white;
}

/* Right Controls */
.right-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.control-group {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.control-label {
  color: var(--gray-400);
  font-size: 0.875rem;
  font-weight: 500;
  white-space: nowrap;
}

.control-input,
.control-select {
  padding: 0.5rem 0.75rem;
  background: var(--gray-800);
  color: white;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  font-size: 0.875rem;
  outline: none;
  transition: all 0.2s;
}

.control-input {
  width: 140px;
}

.control-select {
  width: 130px;
}

.control-input:focus,
.control-select:focus {
  border-color: var(--haste-primary);
  background: var(--gray-700);
}

.theme-select {
  background: var(--gray-700);
}

.file-extension {
  color: var(--gray-400);
  font-size: 0.875rem;
}

/* Action Buttons */
.action-btn {
  padding: 0.5rem 1rem;
  background: transparent;
  color: white;
  border: 1px solid var(--gray-600);
  border-radius: 4px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.action-btn:hover {
  background: var(--gray-700);
  border-color: var(--gray-500);
}

.action-btn-danger {
  color: #ef4444;
  border-color: rgba(239, 68, 68, 0.3);
}

.action-btn-danger:hover {
  background: rgba(239, 68, 68, 0.1);
  border-color: #ef4444;
}

/* Main Content */
.main-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  padding: 1.5rem;
  flex: 1;
  overflow: hidden;
  max-width: 1920px;
  margin: 0 auto;
  width: 100%;
}

.editor-section,
.preview-section {
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.hidden-mobile {
  display: none;
}

/* Preview Card */
.preview-card {
  display: flex;
  flex-direction: column;
  height: 100%;
  background: var(--gray-900);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  overflow: hidden;
}

.preview-header {
  padding: 1rem 1.25rem;
  background: var(--gray-800);
  border-bottom: 1px solid var(--border-color);
}

.preview-title {
  margin: 0;
  color: white;
  font-size: 1.1rem;
  font-weight: 600;
}

.preview-body {
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

/* Bottom Bar */
.bottom-bar {
  background: var(--gray-900);
  border-top: 1px solid var(--border-color);
  padding: 1rem 1.5rem;
  flex-shrink: 0;
}

.bottom-bar-content {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;
  max-width: 1920px;
  margin: 0 auto;
}

.mobile-toggle {
  padding: 0.75rem 1.5rem;
  background: transparent;
  color: white;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.mobile-toggle:hover {
  background: var(--gray-800);
  border-color: var(--haste-primary);
}

/* Fade Transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Mobile Responsive */
@media (max-width: 768px) {
  .control-bar-content {
    flex-direction: column;
    align-items: stretch;
    gap: 1rem;
  }

  .mode-tabs {
    width: 100%;
  }

  .mode-tab {
    flex: 1;
    text-align: center;
  }

  .right-controls {
    flex-direction: column;
    align-items: stretch;
    gap: 0.75rem;
  }

  .control-group {
    justify-content: space-between;
  }

  .action-btn {
    width: 100%;
  }

  .main-content {
    grid-template-columns: 1fr;
    padding: 1rem;
  }
}

/* Scrollbar Styling */
:deep(*::-webkit-scrollbar) {
  width: 8px;
  height: 8px;
}

:deep(*::-webkit-scrollbar-track) {
  background: var(--gray-800);
}

:deep(*::-webkit-scrollbar-thumb) {
  background: var(--haste-red);
  border-radius: 4px;
}

:deep(*::-webkit-scrollbar-thumb:hover) {
  background: #ff453a;
}
</style>
