<template>
  <AppHeader />
  <main>
    <CookieConsent />
    <!-- This shows the banner if consent isn't given yet -->
    <router-view></router-view>
  </main>
  <FooterComponent />
</template>

<script setup>
import AppHeader from "@/components/AppHeader.vue";
import FooterComponent from "@/components/FooterComponent.vue";
import CookieConsent from "@/components/CookieConsent.vue";
</script>

<script>
export default {
  useHead: {
    titleTemplate: "%s - HasteCV",
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { property: "og:site_name", content: "HasteCV" },
      { property: "og:type", content: "website" }
    ]
  }
};
</script>
