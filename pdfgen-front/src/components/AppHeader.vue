<template>
  <header
    class="center bg-transparent py-8 font-open-sans font-bold text-white"
  >
    <div class="flex items-center justify-between">
      <!-- Clickable Logo -->
      <router-link to="/" class="logo-link">
        <h1 class="logo">HasteCV</h1>
      </router-link>

      <!-- Call to Action Button -->
      <button @click="navigateToApp" class="haste-button">Build Now</button>
    </div>
  </header>
</template>

<script setup>
import { useRouter } from "vue-router";

const router = useRouter();

function navigateToApp() {
  router.push("/app"); // Navigate to the app's main page
}
</script>

<style scoped>
/* Styles for the clickable logo */
.logo-link {
  text-decoration: none;
}

h1.logo {
  font-size: 3rem;
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

.haste-button {
  font-size: 1.5rem;
  background-color: var(--haste-yellow);
  color: var(--primary-black);
  border-radius: 2px;
}

.haste-button:hover {
  background-color: transparent;
  color: var(--haste-yellow);

}
</style>
