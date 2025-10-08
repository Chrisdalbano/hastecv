<template>
  <select
    :class="cn(
      'flex h-10 w-full rounded-md border border-gray-700 bg-gray-900/50 px-3 py-2 text-sm text-white ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--haste-yellow)] focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50',
      props.class
    )"
    v-bind="$attrs"
  >
    <slot />
  </select>
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

