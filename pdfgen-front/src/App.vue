<template>
  <AppHeader />
  <main>
    <router-view></router-view>
  </main>
  <FooterComponent />
</template>

<script setup>
import AppHeader from "@/components/AppHeader.vue";
import FooterComponent from "./components/FooterComponent.vue";
</script>

<style></style>
