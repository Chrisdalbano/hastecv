<template>
  <AppHeader />
  <main>
    <router-view v-slot="{ Component }">
      <Transition name="fade">
        <component :is="Component" />
      </Transition>
    </router-view>
  </main>
</template>

<script setup>
import AppHeader from "@/components/AppHeader.vue";
</script>

<style>
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.fade-enter-active, .fade-leave-active {
  opacity: 1;
  transition: opacity 0.3s ease-in-out;
}

</style>
