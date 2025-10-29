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
            <component v-if="mode.icon" :is="mode.icon" class="mode-icon" />
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

         

          <!-- Language Selector -->
          <div class="control-group">
            <label class="control-label">
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" style="display: inline-block; vertical-align: middle; margin-right: 4px;">
                <circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="1.5" fill="none"/>
                <path d="M2 8h12M8 2c1.5 2 1.5 4 1.5 6s0 4-1.5 6M8 2C6.5 4 6.5 6 6.5 8s0 4 1.5 6" stroke="currentColor" stroke-width="1.5"/>
              </svg>
              Language
            </label>
            <select
              v-model="store.language"
              class="control-select"
            >
              <option value="en">🇺🇸 English</option>
              <option value="es">🇪🇸 Español</option>
              <option value="fr">🇫🇷 Français</option>
              <option value="de">🇩🇪 Deutsch</option>
              <option value="pt">🇵🇹 Português</option>
            </select>
          </div>

          <!-- Action Buttons -->
          <button @click="injectDummyData" class="action-btn">
            <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
              <path d="M9 3.75V14.25M3.75 9H14.25" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
            Load Test Data
          </button>
          <button @click="clearData" class="action-btn action-btn-danger">
            <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
              <path d="M13.5 4.5L4.5 13.5M4.5 4.5L13.5 13.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
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

      <!-- Customization Sidebar (Physical space) -->
      <SimplifiedCustomization ref="customizationPanelRef" />
    </div>

    <!-- Mobile Backdrop (overlay when sidebar is open) -->
    <div v-if="isMobile" class="mobile-backdrop" :class="{ 'active': customizationPanelRef?.isOpen }" @click="closeSidebar"></div>

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
        <GenerateButton ref="generateButtonRef" :customizationPanel="customizationPanelRef" />
      </div>
    </div>
  </div>
</template>

<script setup>
import PreviewCV from "@/components/home/PreviewCV.vue";
import GenerateButton from "@/components/GenerateButton.vue";
import SimplifiedCustomization from "@/components/SimplifiedCustomization.vue";
import { useResumeDataStore } from "../stores/resumeData";
import { useThemeStore } from "../stores/themeStore";
import { ref, onMounted, onUnmounted, watch, defineComponent, h } from "vue";
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

// Refs and reactive state
const isMobile = ref(window.innerWidth <= 768);
const isPreviewVisible = ref(false);
const currentRoute = ref(route.path);
const customizationPanelRef = ref(null);
const generateButtonRef = ref(null);
let debounceTimer = null;

onUnmounted(() => {
  window.removeEventListener("resize", checkWindowSize);
  if (debounceTimer) {
    clearTimeout(debounceTimer);
  }
});

// Auto-regenerate PDF when theme/layout changes
const autoRegenerate = () => {
  // Only auto-regenerate if we have a download link (PDF was generated at least once)
  if (!store.downloadLink || !store.consentAccepted) {
    return;
  }
  
  // Clear existing timer
  if (debounceTimer) {
    clearTimeout(debounceTimer);
  }
  
  // Set new timer (1 second debounce)
  debounceTimer = setTimeout(async () => {
    if (generateButtonRef.value && !generateButtonRef.value.isGenerating) {
      try {
        await generateButtonRef.value.handleGenerate();
      } catch (error) {
        console.error('Auto-regeneration error:', error);
      }
    }
  }, 1000);
};

// Watch for theme changes
watch(() => themeStore.pdfTheme, autoRegenerate);
watch(() => themeStore.pdfCustomColor, autoRegenerate);

// Watch for layout/spacing changes (via customization panel ref)
// Wait for component to mount before setting up watch
watch(() => customizationPanelRef.value, (newVal) => {
  if (newVal && newVal.getLayoutSettings) {
    // Now we can watch layout settings changes
    watch(() => {
      try {
        return newVal.getLayoutSettings ? JSON.stringify(newVal.getLayoutSettings()) : null;
      } catch (e) {
        return null;
      }
    }, autoRegenerate);
  }
});

// Mode icons
const ManualIcon = defineComponent({
  render() {
    return h('svg', { width: '18', height: '18', viewBox: '0 0 18 18', fill: 'none' }, [
      h('path', { d: 'M7.5 3.75H3.75V7.5H7.5V3.75ZM14.25 3.75H10.5V7.5H14.25V3.75ZM7.5 10.5H3.75V14.25H7.5V10.5ZM14.25 10.5H10.5V14.25H14.25V10.5Z', stroke: 'currentColor', 'stroke-width': '1.5', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' })
    ]);
  }
});

const JSONIcon = defineComponent({
  render() {
    return h('svg', { width: '18', height: '18', viewBox: '0 0 18 18', fill: 'none' }, [
      h('path', { d: 'M4.5 3.75L2.25 6L4.5 8.25M13.5 3.75L15.75 6L13.5 8.25M10.5 2.25L7.5 11.25', stroke: 'currentColor', 'stroke-width': '1.5', 'stroke-linecap': 'round', 'stroke-linejoin': 'round' })
    ]);
  }
});

const VisualIcon = defineComponent({
  render() {
    return h('svg', { width: '18', height: '18', viewBox: '0 0 18 18', fill: 'none' }, [
      h('rect', { x: '3', y: '3', width: '12', height: '12', rx: '1.5', stroke: 'currentColor', 'stroke-width': '1.5' }),
      h('path', { d: 'M3 7.5H15M9 7.5V15', stroke: 'currentColor', 'stroke-width': '1.5' })
    ]);
  }
});

const modes = [
  { path: '/app', label: 'Manual', icon: ManualIcon },
  { path: '/app/json', label: 'JSON', icon: JSONIcon },
  { path: '/app/visual', label: 'Visual Builder', icon: VisualIcon }
];


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

function closeSidebar() {
  if (customizationPanelRef.value && customizationPanelRef.value.isOpen) {
    customizationPanelRef.value.isOpen = false;
  }
}
</script>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: visible; /* Allow sidebar content to be visible */
}

/* Control Bar */
.control-bar {
  background: var(--gray-900);
  border-bottom: 1px solid var(--border-color);
  padding: 1rem 1.5rem;
  flex-shrink: 0;
}

/* Simplified - removed tab system, now using floating sidebar */

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
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 1.25rem;
  background: transparent;
  color: white;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.9375rem;
  cursor: pointer;
  transition: all 0.2s;
}

.mode-icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
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
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background: transparent;
  color: white;
  border: 1px solid var(--gray-600);
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.875rem;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.action-btn svg {
  flex-shrink: 0;
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
  grid-template-columns: 1fr 1fr auto;
  gap: 1.5rem;
  padding-left: 1.5rem;
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
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  min-height: 0;
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

/* Mobile Backdrop */
.mobile-backdrop {
  display: none;
}

/* Mobile Responsive */
/* ============================================
   TABLET RESPONSIVE (768px - 1024px)
   ============================================ */
@media (max-width: 1024px) and (min-width: 769px) {
  .main-content {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .customization-sidebar {
    position: fixed;
    right: 0;
    top: 0;
    height: 100vh;
    z-index: 1000;
    transform: translateX(100%);
    transition: transform 0.3s ease;
  }

  .customization-sidebar.is-open {
    transform: translateX(0);
    box-shadow: -4px 0 20px rgba(0, 0, 0, 0.5);
  }
}

/* ============================================
   MOBILE RESPONSIVE (< 768px)
   Completely different UX with bottom sheet
   ============================================ */
@media (max-width: 768px) {
  /* Control Bar - Ultra Compact */
  .control-bar {
    padding: 0.5rem 0.75rem;
  }

  .control-bar-content {
    flex-direction: row;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
  }

  /* Mode Tabs - Horizontal Pills */
  .mode-tabs {
    flex: 1;
    min-width: 0;
    overflow-x: auto;
    scrollbar-width: none;
    gap: 0.25rem;
  }

  .mode-tabs::-webkit-scrollbar {
    display: none;
  }

  .mode-tab {
    flex: 0 0 auto;
    min-width: auto;
    padding: 0.5rem 0.75rem;
    font-size: 0.8125rem;
    border-radius: 20px;
  }

  .mode-tab svg {
    width: 16px;
    height: 16px;
  }

  .mode-tab span {
    display: none; /* Icons only */
  }

  /* Hide right controls on mobile - use settings menu instead */
  .right-controls {
    display: none;
  }

  /* Main Content - Mobile Tabs */
  .main-content {
    grid-template-columns: 1fr;
    padding: 0;
    gap: 0;
    position: relative;
    height: calc(100vh - 48px - 70px); /* Control bar + bottom bar */
  }

  .editor-section,
  .preview-section {
    display: none;
    height: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    padding: 0.75rem;
    -webkit-overflow-scrolling: touch;
  }

  .editor-section:not(.hidden-mobile) {
    display: flex;
    flex-direction: column;
  }

  .preview-section:not(.hidden-mobile) {
    display: flex;
    flex-direction: column;
  }

  /* Make forms more mobile-friendly */
  .editor-section :deep(input),
  .editor-section :deep(textarea),
  .editor-section :deep(select) {
    font-size: 16px !important; /* Prevents zoom on iOS */
    -webkit-appearance: none;
    appearance: none;
  }

  .editor-section :deep(textarea) {
    min-height: 100px;
  }

  /* Manual Form - Beautiful Mobile Experience */
  .editor-section :deep(.resume-form),
  .editor-section :deep(.manual-editor),
  .editor-section :deep(.manual-form) {
    padding: 0 !important;
    width: 100% !important;
  }

  /* Form sections with proper spacing */
  .editor-section :deep(.form-section),
  .editor-section :deep(.section-card),
  .editor-section :deep([class*="section"]):not(.editor-section) {
    margin-bottom: 1.25rem !important;
    background: var(--gray-800) !important;
    border: 2px solid var(--gray-700) !important;
    border-radius: 16px !important;
    overflow: visible !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
    position: relative !important;
  }

  /* Section headers - no overlap */
  .editor-section :deep(.form-section-header),
  .editor-section :deep(.section-header),
  .editor-section :deep(h3),
  .editor-section :deep(h2) {
    padding: 1rem !important;
    background: var(--haste-primary) !important;
    border-bottom: none !important;
    border-radius: 14px 14px 0 0 !important;
    font-weight: 700 !important;
    font-size: 0.9375rem !important;
    color: white !important;
    text-transform: uppercase !important;
    letter-spacing: 0.75px !important;
    margin: 0 !important;
    position: relative !important;
    z-index: 1 !important;
    display: block !important;
    width: 100% !important;
  }

  /* Remove emoji pseudo-element causing overlap */
  .editor-section :deep(.section-header)::before,
  .editor-section :deep(h3)::before {
    content: none !important;
  }

  /* Form content area */
  .editor-section :deep(.form-section-content),
  .editor-section :deep(.section-content),
  .editor-section :deep([class*="content"]) {
    padding: 1.25rem 1rem !important;
    background: var(--gray-800) !important;
    border-radius: 0 0 14px 14px !important;
  }

  .editor-section :deep(.form-group),
  .editor-section :deep(.input-group),
  .editor-section :deep([class*="group"]) {
    margin-bottom: 1.25rem !important;
    position: relative !important;
  }

  .editor-section :deep(.form-group):last-child,
  .editor-section :deep(.input-group):last-child {
    margin-bottom: 0 !important;
  }

  /* Labels - clear and readable */
  .editor-section :deep(label) {
    display: block !important;
    margin-bottom: 0.625rem !important;
    font-size: 0.8125rem !important;
    font-weight: 700 !important;
    color: white !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    line-height: 1.4 !important;
  }

  /* Input fields - clean and modern */
  .editor-section :deep(input[type="text"]),
  .editor-section :deep(input[type="email"]),
  .editor-section :deep(input[type="tel"]),
  .editor-section :deep(input[type="url"]),
  .editor-section :deep(input[type="date"]),
  .editor-section :deep(textarea),
  .editor-section :deep(select) {
    width: 100% !important;
    padding: 0.875rem 1rem !important;
    border: 2px solid var(--gray-600) !important;
    border-radius: 10px !important;
    background: var(--gray-900) !important;
    color: white !important;
    font-size: 16px !important;
    font-weight: 400 !important;
    line-height: 1.5 !important;
    transition: all 0.2s ease !important;
    -webkit-appearance: none !important;
    box-sizing: border-box !important;
  }

  /* Focus state - simplified */
  .editor-section :deep(input:focus),
  .editor-section :deep(textarea:focus),
  .editor-section :deep(select:focus) {
    outline: none !important;
    border-color: var(--haste-primary) !important;
    background: var(--gray-900) !important;
    box-shadow: 0 0 0 3px rgba(255, 69, 58, 0.2) !important;
  }

  .editor-section :deep(textarea) {
    min-height: 120px !important;
    resize: vertical !important;
    line-height: 1.6 !important;
  }

  /* Buttons in forms - Touch Friendly */
  .editor-section :deep(button) {
    min-height: 48px !important;
    font-size: 0.9375rem !important;
    font-weight: 600 !important;
    padding: 0.75rem 1.25rem !important;
    border-radius: 10px !important;
    transition: all 0.2s ease !important;
    border: none !important;
    cursor: pointer !important;
  }

  .editor-section :deep(button:active) {
    transform: scale(0.97) !important;
  }

  /* Primary buttons (Add) */
  .editor-section :deep(button[class*="add"]),
  .editor-section :deep(.add-button) {
    background: var(--haste-primary) !important;
    color: white !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 8px rgba(255, 69, 58, 0.3) !important;
  }

  /* Secondary buttons (Remove/Delete) */
  .editor-section :deep(button[class*="remove"]),
  .editor-section :deep(button[class*="delete"]),
  .editor-section :deep(.remove-button),
  .editor-section :deep(.delete-button) {
    background: var(--gray-700) !important;
    color: white !important;
    border: 1px solid var(--gray-600) !important;
  }

  /* Array/List items */
  .editor-section :deep(.array-item),
  .editor-section :deep([class*="item-container"]) {
    background: var(--gray-900) !important;
    border: 1px solid var(--gray-700) !important;
    border-radius: 10px !important;
    padding: 1rem !important;
    margin-bottom: 1rem !important;
    position: relative !important;
  }

  /* Checkboxes & Radio buttons */
  .editor-section :deep(input[type="checkbox"]),
  .editor-section :deep(input[type="radio"]) {
    width: 20px !important;
    height: 20px !important;
    min-width: 20px !important;
    margin-right: 0.625rem !important;
    accent-color: var(--haste-primary) !important;
  }

  /* Helper text */
  .editor-section :deep(.input-hint),
  .editor-section :deep(.hint-text),
  .editor-section :deep(small) {
    font-size: 0.75rem !important;
    color: var(--gray-400) !important;
    margin-top: 0.375rem !important;
    display: block !important;
    line-height: 1.4 !important;
  }

  /* Mobile Backdrop */
  .mobile-backdrop {
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(4px);
    z-index: 1000;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
  }

  .mobile-backdrop.active {
    opacity: 1;
    pointer-events: all;
  }

  /* Sidebar as Bottom Sheet */
  .customization-sidebar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    top: auto;
    height: auto;
    max-height: 75vh;
    width: 100%;
    transform: translateY(100%);
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    border-left: none;
    border-top: 1px solid var(--border-color);
    border-radius: 20px 20px 0 0;
    z-index: 1001;
    box-shadow: 0 -8px 32px rgba(0, 0, 0, 0.6);
  }

  .customization-sidebar.is-open {
    transform: translateY(0);
  }

  /* Force FAB to be visible on mobile */
  .customization-sidebar {
    position: static !important; /* Don't hide it */
  }

  .mini-icons {
    position: fixed !important;
    bottom: 90px !important;
    right: 1rem !important;
    display: flex !important;
    flex-direction: row !important;
    padding: 0.625rem !important;
    background: var(--haste-primary) !important;
    border: 3px solid white !important;
    border-radius: 30px !important;
    gap: 0.5rem !important;
    box-shadow: 
      0 0 0 6px rgba(255, 69, 58, 0.3),
      0 10px 30px rgba(255, 69, 58, 0.7), 
      0 6px 16px rgba(0, 0, 0, 0.6) !important;
    z-index: 99999 !important;
    animation: pulse-glow 2s ease-in-out infinite !important;
    pointer-events: all !important;
  }

  @keyframes pulse-glow {
    0%, 100% {
      box-shadow: 
        0 0 0 6px rgba(255, 69, 58, 0.3),
        0 10px 30px rgba(255, 69, 58, 0.7), 
        0 6px 16px rgba(0, 0, 0, 0.6);
      transform: scale(1);
    }
    50% {
      box-shadow: 
        0 0 0 8px rgba(255, 69, 58, 0.4),
        0 14px 40px rgba(255, 69, 58, 0.9), 
        0 8px 20px rgba(0, 0, 0, 0.7);
      transform: scale(1.05);
    }
  }

  .mini-icon {
    width: 48px !important;
    height: 48px !important;
    border-radius: 24px !important;
    background: white !important;
    border: none !important;
    color: var(--haste-primary) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 22px !important;
    flex-shrink: 0 !important;
  }

  .mini-icon svg {
    width: 24px !important;
    height: 24px !important;
  }

  .mini-icon:active {
    transform: scale(0.9) !important;
    background: rgba(255, 255, 255, 0.85) !important;
  }

  /* Bottom Sheet Content */
  .sidebar-content {
    max-height: 75vh;
    overflow-y: auto;
    border-radius: 20px 20px 0 0;
  }

  .sidebar-header {
    padding: 1.25rem 1rem 1rem;
    position: sticky;
    top: 0;
    background: var(--gray-900);
    z-index: 10;
  }

  .sidebar-header::before {
    content: '';
    position: absolute;
    top: 0.5rem;
    left: 50%;
    transform: translateX(-50%);
    width: 48px;
    height: 5px;
    background: var(--gray-600);
    border-radius: 3px;
  }

  .sidebar-header h3 {
    font-size: 1.125rem;
  }

  /* Bottom Bar - Compact Fixed */
  .bottom-bar {
    padding: 0.625rem 0.75rem;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: var(--gray-900);
    border-top: 1px solid var(--border-color);
    z-index: 100;
    box-shadow: 0 -4px 12px rgba(0, 0, 0, 0.4);
    height: 70px;
  }

  .bottom-bar-content {
    max-width: 100%;
    display: flex;
    gap: 0.5rem;
    align-items: stretch;
  }

  .mobile-toggle {
    flex: 1;
    min-height: 44px;
    font-size: 0.9375rem;
    font-weight: 600;
    border-radius: 10px;
    padding: 0 1rem;
  }

  /* Generate button on mobile */
  .bottom-bar :deep(.generate-button) {
    flex: 2;
    min-height: 44px;
    font-size: 0.9375rem;
    font-weight: 700;
  }

  /* Preview Card - Full Height */
  .preview-card {
    height: 100%;
    border-radius: 0;
    border: none;
    background: transparent;
  }

  .preview-header {
    display: none; /* Hide on mobile to save space */
  }

  .preview-body {
    flex: 1;
    overflow-y: auto;
    padding: 0.5rem;
    height: 100%;
  }

  /* PDF Preview iframe/embed - Full width on mobile */
  .preview-body :deep(iframe),
  .preview-body :deep(embed),
  .preview-body :deep(object) {
    width: 100% !important;
    height: 100% !important;
    border-radius: 8px;
  }

  /* Hide GPT Widget on Mobile */
  :deep(.gpt-chat-widget),
  :deep(.gpt-widget-fab),
  :deep(.gpt-widget-container),
  :deep([class*="gpt"]) {
    display: none !important;
  }

  /* Remove JSON/Visual builder deep styles - let components handle it */

  .editor-section :deep(.instructions-banner) {
    padding: 1rem;
    font-size: 0.875rem;
  }

  .editor-section :deep(.instructions-title) {
    font-size: 1.125rem;
    margin-bottom: 0.5rem;
  }

  .editor-section :deep(.instructions-text) {
    font-size: 0.8125rem;
  }

  .editor-section :deep(.builder-layout) {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .editor-section :deep(.sections-panel),
  .editor-section :deep(.preview-panel) {
    max-height: none;
  }

  .editor-section :deep(.section-item) {
    padding: 0.75rem;
  }

  .editor-section :deep(.section-controls button) {
    min-width: 40px;
    min-height: 40px;
  }

  .editor-section :deep(.add-section-menu) {
    grid-template-columns: 1fr;
  }

  /* JSON Editor Mobile */
  .editor-section :deep(.json-editor-container) {
    font-size: 14px;
  }
}

/* Extra Small Phones */
@media (max-width: 480px) {
  .mode-tab span {
    display: none;
  }

  .mode-tab {
    padding: 0.5rem;
  }

  .customization-sidebar {
    max-height: 85vh;
  }

  .sidebar-content {
    max-height: 85vh;
  }

  .control-label svg {
    width: 14px;
    height: 14px;
  }

  .mini-icons {
    right: 0.5rem;
    bottom: 70px;
  }

  .mini-icon {
    width: 44px;
    height: 44px;
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
