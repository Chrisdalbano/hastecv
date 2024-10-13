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
        <div class="grid grid-cols-1 gap-8 md:grid-cols-3">
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
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import jsonIcon from "../assets/json.svg";
import freeIcon from "../assets/free.svg";
import easyIcon from "../assets/easy.svg";

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
  width: 320px;
  height: 380px;
  padding: 20px;
  color: whitesmoke;
  background: transparent;
  border: 2px solid var(--haste-yellow);
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transform-origin: center center;
  transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.card:hover {
  border-radius: 12px;
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
  font-size: 32px;
  font-weight: 400;
  line-height: 1.2;
}

.card .description {
  font-size: 18px;
  opacity: 0.85;
}
</style>
