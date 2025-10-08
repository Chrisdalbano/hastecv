<template>
  <TabsRoot v-bind="forwarded">
    <slot />
  </TabsRoot>
</template>

<script setup>
import { TabsRoot, useForwardPropsEmits } from 'radix-vue';

const props = defineProps({
  defaultValue: String,
  modelValue: String,
  orientation: String
});

const emits = defineEmits(['update:modelValue']);

const forwarded = useForwardPropsEmits(props, emits);
</script>

