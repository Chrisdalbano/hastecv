<template>
  <div class="bg-primary-black text-whitesmoke font-OpenSans">
    <!-- Hero Section -->
    <section class="hero bg-primary-black text-whitesmoke py-20">
      <div class="center px-4 text-center">
        <h1
          class="font-Anton mb-6 text-6xl font-extrabold leading-tight drop-shadow-2xl text-haste-yellow"
        >
          Craft ATS-Beating CVs in Minutes
        </h1>
        <p
          class="font-Domine text-whitesmoke mx-auto mb-8 max-w-2xl text-lg leading-relaxed opacity-90 md:text-xl"
        >
          Effortlessly create professional, ATS-passing CV templates that help
          you land your dream job. Customize every detail manually or with JSON
          for full control.
        </p>

        <!-- Updated animated call-to-action button -->
        <div class="flex justify-center">
          <button @click="navigateToApp" class="animated-button">
            <svg
              viewBox="0 0 24 24"
              class="arr-2"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M16.1716 10.9999L10.8076 5.63589L12.2218 4.22168L20 11.9999L12.2218 19.778L10.8076 18.3638L16.1716 12.9999H4V10.9999H16.1716Z"
              ></path>
            </svg>
            <span class="text">Start Crafting Resume</span>
            <span class="circle"></span>
            <svg
              viewBox="0 0 24 24"
              class="arr-1"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M16.1716 10.9999L10.8076 5.63589L12.2218 4.22168L20 11.9999L12.2218 19.778L10.8076 18.3638L16.1716 12.9999H4V10.9999H16.1716Z"
              ></path>
            </svg>
          </button>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features py-20">
      <div class="center text-center">
        <h2 class="mb-12 text-3xl font-bold text-haste-yellow">Why HasteCV?</h2>
        <div class="grid gap-8">
          <div v-for="(feature, index) in features" :key="index" class="card">
            <div class="illustration-container">
              <img
                :src="feature.image"
                alt="Feature Icon"
                class="illustration"
              />
            </div>
            <div class="main-content">
              <h3 class="heading">{{ feature.title }}</h3>
              <p class="description">{{ feature.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="how-it-works text-whitesmoke bg-gray-800 py-20">
      <div class="center">
        <h2 class="mb-12 text-center text-3xl font-bold text-haste-yellow">
          How HasteCV Works
        </h2>
        <ol class="mx-auto max-w-4xl list-inside space-y-8 text-left">
          <li>
            <h3 class="mb-2 text-2xl font-bold">Choose Your Template</h3>
            <p class="text-lg leading-relaxed">
              Begin by selecting a template that best suits the type of job you
              are applying for. HasteCV offers a couple of templates, giving you
              some flexibility to match your resume with your desired industry.
              Don't know how to start? Generate some 'Test Data' to get some
              inspiration.
            </p>
          </li>
          <li>
            <h3 class="mb-2 text-2xl font-bold">Customize Your CV</h3>
            <p class="text-lg leading-relaxed">
              Use our editor to manually input your personal details, work
              experience, and skills, or take advantage of JSON editing for
              advanced customization. Personalize every detail to stand out from
              the competition.
            </p>
          </li>
          <li>
            <h3 class="mb-2 text-2xl font-bold">
              Generated & Optimized for ATS
            </h3>
            <p class="text-lg leading-relaxed">
              When ready, click the GENERATE button to create your resume. With
              HasteCV, the structure of your resume will be automatically
              optimized for Applicant Tracking Systems (ATS). It structures your
              resume to pass through ATS scans effectively, ensuring it reaches
              hiring managers.
            </p>
          </li>
          <li>
            <h3 class="mb-2 text-2xl font-bold">Download & Apply</h3>
            <p class="text-lg leading-relaxed">
              Once satisfied with your CV, download it as a PDF. Your
              professionally crafted, ATS-ready CV is now ready to send out to
              potential employers and help you land that dream job.
            </p>
          </li>
        </ol>
      </div>
    </section>

    <!-- Additional Tips & Resources Section -->
    <section class="tips-resources text-whitesmoke py-20">
      <div class="center">
        <h2 class="mb-12 text-center text-3xl font-bold text-haste-yellow">
          Tips & Resources for a Winning CV
        </h2>
        <div class="mx-auto max-w-4xl space-y-8 text-left">
          <div>
            <h3 class="mb-2 text-2xl font-bold">Top CV Writing Tips</h3>
            <p class="text-lg leading-relaxed">
              Crafting a winning CV is about showcasing your experience and
              skills in a clear, concise manner. Here are some top tips:
            </p>
            <ul class="mt-2 list-inside list-disc space-y-2">
              <li>Focus on your achievements, not just duties.</li>
              <li>Keep it concise – one to two pages are ideal.</li>
              <li>
                Tailor your CV to the job description for every application.
              </li>
              <li>
                Use action verbs to describe your experience (e.g., led,
                improved, created).
              </li>
            </ul>
          </div>
          <div>
            <h3 class="mb-2 text-2xl font-bold">What is JSON Editing</h3>
            <p class="text-lg leading-relaxed">
              JSON editing allows advanced customization of your CV. This
              feature is perfect for tech-savvy users who want complete control
              over the CV layout. With JSON, you can directly modify the data
              structure to fit specific needs, ensuring no detail is overlooked.
            </p>
          </div>

          <!-- Collapsible JSON Example Section -->
          <div class="json-example text-whitesmoke">
            <h3 class="mb-2 text-2xl font-bold">JSON is also customizable!</h3>
            <p class="mb-6 text-lg leading-relaxed">
              Take a look at my updated CV crafted using HasteCV below, you can use it as
              a reference and see how fields like 'technical-proficiency' and
              'projects' can be added:
            </p>

            <!-- Collapsible JSON Container -->
            <div class="json-container">
              <div ref="jsonContent" class="json-content">
                <pre><code>{{ formattedJson }}</code></pre>
              </div>

              <!-- Toggle Button -->
              <button @click="toggleJsonView" class="toggle-json-btn">
                {{ isExpanded ? "Collapse JSON" : "Expand JSON" }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { ref, onMounted } from "vue";
import { gsap } from "gsap";
import jsonIcon from "../assets/json.svg";
import freeIcon from "../assets/free.svg";
import easyIcon from "../assets/easy.svg";
// Import the JSON data dynamically
import resumeData from "@/assets/resumeData.json";

const router = useRouter();

const features = [
  {
    title: "Quick & Easy",
    description:
      "Create your CV in just a few clicks using our intuitive editor.",
    image: easyIcon
  },
  {
    title: "It's Free!",
    description:
      "Use it freely. No strings attached! We don't collect data and we don't store your information.",
    image: freeIcon
  },
  {
    title: "Edit with JSON",
    description:
      "For advanced users, directly modify your CV structure with JSON.",
    image: jsonIcon
  }
];

function navigateToApp() {
  router.push("/app");
}

// State for collapsible JSON
const isExpanded = ref(false);
const jsonContent = ref(null);

// GSAP animation for expanding/collapsing JSON
const toggleJsonView = () => {
  if (isExpanded.value) {
    gsap.to(jsonContent.value, { height: "200px", duration: 1 });
  } else {
    gsap.to(jsonContent.value, { height: "auto", duration: 1 });
  }
  isExpanded.value = !isExpanded.value;
};

// Format JSON for display
const formattedJson = JSON.stringify(resumeData, null, 2);

onMounted(() => {
  gsap.set(jsonContent.value, { height: "200px", overflow: "hidden" });
});
</script>

<script>
export default {
  useHead: {
    title: "HasteCV - Professional CV Builder",
    meta: [
      {
        name: "description",
        content:
          "Craft professional, ATS-ready resumes in minutes. HasteCV offers quick, easy, and free CV-building tools."
      },
      {
        name: "keywords",
        content:
          "resume builder, ATS resume, job application, CV builder, resume templates"
      },
      { property: "og:title", content: "HasteCV - Professional CV Builder" },
      {
        property: "og:description",
        content:
          "Create ATS-passing resumes with HasteCV, offering fast and free CV-building tools."
      }
    ]
  }
};
</script>

<style scoped>
.center {
  width: min(100% - 2rem, 1200px);
  margin-inline: auto;
  padding-inline: 1rem;
}

/* Hero Section Styling */
.hero {
  background: var(--primary-black);
  position: relative;
  color: whitesmoke;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.8);
}

/* Animated button styling */
.animated-button {
  position: relative;
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 16px 36px;
  border: 4px solid transparent;
  font-size: 18px;
  background-color: transparent;
  border-radius: 2px;
  font-weight: 600;
  color: var(--haste-yellow);
  box-shadow: 0 0 0 2px var(--haste-yellow);
  cursor: pointer;
  overflow: hidden;
  transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button svg {
  position: absolute;
  width: 24px;
  fill: var(--haste-yellow);
  z-index: 9;
  transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button .arr-1 {
  right: 16px;
}

.animated-button .arr-2 {
  left: -25%;
}

.animated-button .circle {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 20px;
  height: 20px;
  background-color: var(--haste-yellow);
  border-radius: 50%;
  opacity: 0;
  transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button .text {
  position: relative;
  z-index: 1;
  transform: translateX(-12px);
  transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
}

.animated-button:hover {
  box-shadow: 0 0 0 12px transparent;
  color: var(--primary-black);
  border-radius: 12px;
}

.animated-button:hover .arr-1 {
  right: -25%;
}

.animated-button:hover .arr-2 {
  left: 16px;
}

.animated-button:hover .text {
  transform: translateX(12px);
}

.animated-button:hover svg {
  fill: var(--primary-black);
}

.animated-button:active {
  scale: 0.95;
  box-shadow: 0 0 0 4px var(--haste-yellow);
}

.animated-button:hover .circle {
  width: 250px;
  height: 220px;
  opacity: 1;
}

/* Card styling */
.card {
  border-radius: 8px;
  width: 100%;
  height: auto;
  padding: 20px;
  color: whitesmoke;
  background: transparent;
  border: 2px solid var(--haste-yellow);
  display: flex;
  flex-direction: column;
  transform-origin: center center;
  transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.card:hover {
  border-radius: 8px;
  background-color: var(--haste-yellow);
  scale: 0.95;
  rotate: 8deg;
  box-shadow: 0px 3px 187.5px 7.5px rgba(255, 107, 0, 0.4);
}

.illustration-container {
  height: 150px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.illustration {
  max-width: 140px;
  max-height: 140px;
}

.card .main-content {
  flex: 1;
}

.card .heading {
  font-size: 24px;
  font-weight: 600;
  line-height: 1.2;
  margin-bottom: 8px;
}

.card .description {
  font-size: 16px;
  opacity: 0.85;
}

/* Updated Grid for Medium and Large Screens */
@media (min-width: 768px) {
  .grid {
    grid-template-columns: repeat(2, minmax(300px, 1fr));
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, minmax(320px, 1fr));
  }
}

/* How-it-works section styling */
.how-it-works {
  padding: 2rem;
  background: var(--primary-black);
  color: whitesmoke;
  border-top: 2px solid var(--haste-yellow);
}

.how-it-works ol {
  counter-reset: step-counter;
}

.how-it-works li {
  position: relative;
  padding-left: 2.5rem;
}

.how-it-works li::before {
  content: counter(step-counter);
  counter-increment: step-counter;
  position: absolute;
  left: 0;
  top: 0;
  width: 2rem;
  height: 2rem;
  background-color: var(--haste-yellow);
  color: var(--primary-black);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

/* Tips & Resources Section Styling */
.tips-resources {
  padding: 2rem;
  background: var(--primary-black);
  color: whitesmoke;
  border-top: 2px solid var(--haste-yellow);
}

.tips-resources .list-disc li a {
  color: var(--haste-yellow);
  text-decoration: none;
  transition: color 0.3s;
}

.tips-resources .list-disc li a:hover {
  text-decoration: underline;
}

/* JSON example container styling */
.json-container {
  background-color: #1e1e1e;
  border: 1px solid var(--haste-yellow);
  border-radius: 8px;
  padding: 16px;
  max-width: 800px;
  margin: 0 auto;
  position: relative;
}

.json-content {
  overflow: hidden;
  max-width: 100%;
  white-space: pre-wrap;
  color: #d1d5db; /* Light gray color for the JSON text */
  font-family: "Fira Code", monospace;
  background: #272822;
  border-radius: 8px;
  padding: 16px;
  transition: height 0.5s ease;
}

.toggle-json-btn {
  background-color: var(--haste-yellow);
  color: var(--primary-black);
  padding: 8px 16px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  margin-top: 12px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.toggle-json-btn:hover {
  background-color: #ffcc00;
}
</style>
