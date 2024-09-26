<template>
  <div
    style="--min-width: 300"
    class="center relative z-10 grid grid-cols-2 gap-4 overflow-hidden p-1 py-4 max-lg:grid-cols-1"
  >
    <div class="space-y-4">
      <div
        class="flex flex-wrap items-center justify-center md:justify-between"
      >
        <!-- padding left to compensate the .center class padding -->
        <div class="switch-toggle">
          <AppLink to="/" class="flex-1">Manual</AppLink>
          <AppLink to="/json" class="flex-1">JSON</AppLink>
        </div>
        <div class="mx-2 flex items-center">
          <label class="text-xl font-bold text-haste-yellow">STYLE:</label>
          <TemplateSelector @select="updateTemplate" />
        </div>
      </div>

      <router-view v-slot="{ Component, route }">
        <Transition mode="out-in" name="fade">
          <component :is="Component" :key="route.path" />
        </Transition>
      </router-view>
    </div>
    <PreviewCV class="min-w-[--min-width]" :downloadLink="store.downloadLink" />
  </div>
</template>
<script setup>
import TemplateSelector from "@/components/home/TemplateSelector.vue";
import PreviewCV from "@/components/home/PreviewCV.vue";
import AppLink from "@/components/AppLink.vue";

import { useResumeDataStore } from "../stores/resumeData";

const store = useResumeDataStore();

function updateTemplate(newTemplate) {
  store.template = newTemplate;
}
</script>

<style scoped>
.switch-toggle {
  --max-width: 260px;
  background: transparent;
  display: flex;
  max-width: var(--max-width);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.25s ease-in-out;
}
</style>
