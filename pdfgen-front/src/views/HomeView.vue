<template>
  <div class="center grid grid-cols-2 max-lg:grid-cols-1">
    <TemplateSelector @select="updateTemplate" />
  </div>
  <div
    style="--min-width: 300"
    class="center relative z-10 grid grid-cols-2 gap-4 overflow-hidden p-1 py-4 max-lg:grid-cols-1"
  >
    <div class="space-y-4">
      <!-- padding left to compensate the .center class padding -->
      <div class="switch-toggle pl-1">
        <AppLink to="/" class="flex-1">Manual</AppLink>
        <AppLink to="/json" class="flex-1">JSON</AppLink>
      </div>
      <RouterView></RouterView>
    </div>
    <PreviewCV class="min-w-[--min-width]" :downloadLink="store.downloadLink" />
  </div>
  <DownloadLink v-if="store.downloadLink" :downloadLink="store.downloadLink" />
</template>
<script setup>
import DownloadLink from "@/components/DownloadLink.vue";
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
</style>
