<template>
  <header
    class="center bg-transparent py-8 font-open-sans font-bold italic text-white"
  >
    <h1 class="logo">HasteCV</h1>
  </header>
</template>

<script setup></script>

<style scoped>
/* Add any scoped styles for Header component here */

h1 {
  color: var(--haste-yellow);
}

h1.logo {
  font-size: 3rem;
  font-family: "Anton", sans-serif;
  font-weight: 400;
  letter-spacing: 2px;
  text-shadow:
    3px 3px 0 #000,
    6px 6px 0 #000,
    9px 9px 0 #000;
  transform: skewX(-20deg);
  -webkit-text-stroke: 2px black;
}
</style>
