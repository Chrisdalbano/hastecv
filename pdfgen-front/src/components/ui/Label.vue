<template>
  <label
    :class="cn(
      'text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 text-white',
      props.class
    )"
    v-bind="$attrs"
  >
    <slot />
  </label>
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

