<!-- GenerateButton.vue -->
<template>
  <button @click="handleGenerate" class="haste-button">GENERATE</button>
</template>

<script setup>
import { useResumeDataStore } from "@/stores/resumeData";
import { ref, watch } from "vue";

const store = useResumeDataStore();
const canGenerate = ref(store.consentAccepted);

// Watching for changes in consent status
watch(
  () => store.consentAccepted,
  (newVal) => {
    canGenerate.value = newVal;
  }
);

function handleGenerate() {
  if (canGenerate.value) {
    store.generatePdf(JSON.stringify(store.resumeData));
  } else {
    alert("You need to accept cookies to generate a resume.");
  }
}
</script>

<style scoped>

</style>
