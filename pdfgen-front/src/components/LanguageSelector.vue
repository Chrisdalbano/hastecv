<template>
  <div class="language-selector">
    <label for="language-select" class="language-label">Language:</label>
    <select
      id="language-select"
      v-model="store.language"
      class="language-select"
      @change="handleLanguageChange"
    >
      <option value="en">🇺🇸 English</option>
      <option value="es">🇪🇸 Español</option>
      <option value="fr">🇫🇷 Français</option>
      <option value="de">🇩🇪 Deutsch</option>
      <option value="pt">🇵🇹 Português</option>
    </select>
  </div>
</template>

<script setup>
import { useResumeDataStore } from "@/stores/resumeData";

const store = useResumeDataStore();

function handleLanguageChange() {
  // Language is automatically saved in the store via the watcher
  console.log("Language changed to:", store.language);
}
</script>

<style scoped>
.language-selector {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 1rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 6px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.language-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--gray-300);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  white-space: nowrap;
}

.language-select {
  padding: 0.5rem 0.75rem;
  background: var(--gray-800);
  color: white;
  border: 1px solid var(--haste-primary);
  border-radius: 4px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s;
  outline: none;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%23ffffff' d='M6 9L1 4h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 0.5rem center;
  padding-right: 2rem;
}

.language-select:hover {
  border-color: var(--haste-primary);
  box-shadow: 0 0 0 2px rgba(var(--haste-primary-rgb), 0.1);
}

.language-select:focus {
  border-color: var(--haste-primary);
  box-shadow: 0 0 0 3px rgba(var(--haste-primary-rgb), 0.2);
}

.language-select option {
  background: var(--gray-900);
  color: white;
}

@media (max-width: 768px) {
  .language-selector {
    gap: 0.5rem;
    padding: 0.4rem 0.75rem;
  }

  .language-label {
    font-size: 0.75rem;
  }

  .language-select {
    font-size: 0.85rem;
    padding: 0.4rem 1.5rem 0.4rem 0.5rem;
  }
}
</style>
