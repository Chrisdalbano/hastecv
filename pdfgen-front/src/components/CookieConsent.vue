<template>
  <div v-if="!store.consentAccepted" class="cookie-consent-banner">
    <p>We use cookies to ensure you get the best experience on our site.</p>
    <button @click="acceptConsent" class="accept-btn">Accept</button>
  </div>
</template>

<script setup>
import { useResumeDataStore } from "@/stores/resumeData";

const store = useResumeDataStore();

function acceptConsent() {
  store.updateConsentStatus(true);
}
</script>

<style scoped>
.cookie-consent-banner {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: var(--primary-black);
  color: whitesmoke;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 100;
}

.accept-btn {
  background-color: var(--haste-yellow);
  color: var(--primary-black);
  border: none;
  padding: 8px 16px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.3s ease;
}

.accept-btn:hover {
  background-color: white;
  color: var(--primary-black);
}
</style>
