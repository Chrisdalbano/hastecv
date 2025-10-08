<template>
  <div :class="cn('rounded-lg border border-gray-700 bg-gray-900/50 backdrop-blur-sm', props.class)">
    <slot />
  </div>
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

