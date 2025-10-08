<template>
  <TabsList
    :class="cn(
      'inline-flex h-10 items-center justify-center rounded-md bg-gray-800 p-1 text-gray-400',
      props.class
    )"
    v-bind="$attrs"
  >
    <slot />
  </TabsList>
</template>

<script setup>
import { TabsList } from 'radix-vue';
import { cn } from '@/lib/utils';

const props = defineProps({
  class: {
    type: String,
    default: ''
  }
});
</script>

