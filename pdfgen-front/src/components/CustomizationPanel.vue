<template>
  <div class="customization-panel">
    <div class="panel-content">
      <div class="panel-sections">
        <!-- Theme Section -->
        <div class="section">
          <ThemeSelector />
        </div>

        <!-- Layout Section -->
        <div class="section">
          <LayoutSelector ref="layoutSelectorRef" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import ThemeSelector from './ThemeSelector.vue';
import LayoutSelector from './LayoutSelector.vue';

const layoutSelectorRef = ref(null);

// Expose method to get layout settings for parent components
defineExpose({
  getLayoutSettings: () => {
    return layoutSelectorRef.value?.getLayoutSettings?.() || null;
  }
});
</script>

<style scoped>
.customization-panel {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.panel-content {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
}

.panel-sections {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 0;
}

.section {
  width: 100%;
}

/* Scrollbar styling */
.panel-content::-webkit-scrollbar {
  width: 8px;
}

.panel-content::-webkit-scrollbar-track {
  background: var(--gray-800);
}

.panel-content::-webkit-scrollbar-thumb {
  background: var(--haste-primary);
  border-radius: 4px;
}

.panel-content::-webkit-scrollbar-thumb:hover {
  background: var(--haste-primary);
  filter: brightness(1.2);
}
</style>

