<template>
  <TabsContent
    :class="cn(
      'mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2',
      props.class
    )"
    v-bind="$attrs"
  >
    <slot />
  </TabsContent>
</template>

<script setup>
import { TabsContent } from 'radix-vue';
import { cn } from '@/lib/utils';

const props = defineProps({
  class: {
    type: String,
    default: ''
  }
});
</script>

