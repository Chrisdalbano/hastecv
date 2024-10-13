<template>
  <div class="bg-primary-black text-whitesmoke font-OpenSans">
    <!-- Hero Section -->
    <section class="hero bg-primary-black text-whitesmoke py-20">
      <div class="center px-4 text-center">
        <h1 class="font-Anton mb-4 text-5xl font-extrabold drop-shadow-lg">
          Create ATS beating CVs in Minutes with HasteCV
        </h1>
        <p class="font-Domine text-whitesmoke mb-6 text-xl opacity-90">
          Fast, easy, and ATS passing CV templates to help you land your dream
          job. Edit manually or through JSON for ultimate control.
        </p>
        <button @click="navigateToApp" class="haste-button hover-effect">
          Start Crafting Resume
        </button>
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
      "Just use it freely. No strings attached! We don't collect data, we don't store your information.",
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

/* Subtle hover effect for buttons */
.haste-button {
  padding: 0.75rem 1.5rem;
  background-color: transparent;
  color: var(--haste-yellow);
  border: 2px solid var(--haste-yellow);
  transition: all 0.3s ease;
  border-radius: 2px;
}

.haste-button:hover {
  background-color: var(--haste-yellow);
  color: var(--primary-black);
  transform: scale(1.05);
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

/* Hover animation for subtle movements */
.hover-effect:hover {
  transform: translateY(-3px);
  transition: all 0.2s ease;
}
</style>
