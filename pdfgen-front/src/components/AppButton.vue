<template>
  <button>
    <slot />
  </button>
</template>

<script setup></script>

<style scoped>
button {
  padding: 10px 24px;
  border: 1px solid var(--haste-yellow);
  font-size: 24px;
  font-weight: 500;
  text-align: center;
  transition:
    background-color 250ms cubic-bezier(0.93, 0.26, 0.07, 0.69),
    color 250ms cubic-bezier(0.93, 0.26, 0.07, 0.69);
}
</style>
