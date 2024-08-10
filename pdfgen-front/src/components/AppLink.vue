<script setup>
import { computed } from "vue";
import { RouterLink } from "vue-router";


const props = defineProps({
  ...RouterLink.props,
  inactiveClass: String,
  exactActiveClass: {
    default: "active-link",
    type: String
  },
  exactInactiveClass: {
    default: "inactive-link",
    type: String
  }
});

const isExternalLink = computed(() => {
  return typeof props.to === "string" && props.to.startsWith("http");
});
</script>

<template>
  <a v-if="isExternalLink" v-bind="$attrs" :href="to" target="_blank">
    <slot />
  </a>
  <router-link
    v-else
    v-bind="$props"
  >
    
      <slot />
  </router-link>
</template>

<style scoped>
a {
  padding: 10px 24px;
  border: 1px solid var(--haste-yellow);
  color: var(--haste-yellow);
  font-size: 24px;
  font-weight: 500;
  text-align: center;
  transition:
    background-color 250ms cubic-bezier(0.93, 0.26, 0.07, 0.69),
    color 250ms cubic-bezier(0.93, 0.26, 0.07, 0.69);
}
</style>
