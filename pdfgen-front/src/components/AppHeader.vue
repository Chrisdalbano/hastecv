<template>
  <nav class="center py-6 font-open-sans font-bold text-white">
    <div class="header-container flex items-center justify-between">
      <!-- Clickable Logo -->
      <router-link to="/" class="logo-link">
        <h1 class="logo">HasteCV</h1>
      </router-link>

      <!-- Call to Action Button -->
      <button @click="navigateToApp" class="haste-button align-middle">
        Build Now
      </button>
    </div>
  </nav>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

function navigateToApp() {
  router.push("/app"); // Navigate to the app's main page
}
</script>

<style scoped>
/* Container that scales with the center class */
.center {
  width: min(100% - 2rem, 1200px);
  margin-inline: auto;
  padding-inline: 1rem;
}

/* Flex container for header */
.header-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
}

/* Logo styles */
.logo-link {
  text-decoration: none;
}

h1.logo {
  font-size: 2.5rem;
  font-family: "Anton", sans-serif;
  font-weight: 400;
  letter-spacing: 2px;
  transform: skewX(-20deg);
  color: var(--haste-yellow);
  transition:
    transform 0.2s ease,
    color 0.2s ease;
}

/* Logo hover effect */
.logo-link:hover h1.logo {
  transform: skewX(0);
  color: var(--haste-yellow);
}

/* Button styles */
.haste-button {
  font-size: 1.2rem;
  padding: 0.5rem 1.5rem;
  background-color: var(--haste-yellow);
  color: var(--primary-black);
  border-radius: 2px;
  border: 2px solid var(--haste-yellow);
  transition: all 0.3s ease;
}

/* Hover effect for button */
.haste-button:hover {
  background-color: transparent;
  color: var(--haste-yellow);
  transform: scale(1.05);
}

/* Responsive design for mobile */
@media (max-width: 768px) {
  /* Adjust logo font size for mobile */
  h1.logo {
    font-size: 2rem;
    margin-bottom: 0.5rem;
  }

  /* Adjust button size for mobile */
  .haste-button {
    font-size: 1rem;
    padding: 0.5rem 1rem;
  }
}
</style>
