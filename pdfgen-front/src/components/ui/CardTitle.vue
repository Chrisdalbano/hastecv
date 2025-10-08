<template>
  <h3 :class="cn('text-2xl font-semibold leading-none tracking-tight text-white', props.class)">
    <slot />
  </h3>
</template>

<script setup>
import { cn } from '@/lib/utils';

const props = defineProps({
  class: {
    type: String,
    default: ''
  }
});
</script>

