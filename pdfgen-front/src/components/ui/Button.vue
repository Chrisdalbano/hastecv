<template>
  <component
    :is="as"
    :class="cn(buttonVariants({ variant, size }), props.class)"
    v-bind="$attrs"
  >
    <slot />
  </component>
</template>

<script setup>
import { computed } from 'vue';
import { cva } from 'class-variance-authority';
import { cn } from '@/lib/utils';

const props = defineProps({
  as: {
    type: [String, Object],
    default: 'button'
  },
  variant: {
    type: String,
    default: 'default'
  },
  size: {
    type: String,
    default: 'default'
  },
  class: {
    type: String,
    default: ''
  }
});

const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-md text-sm font-semibold ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        default: 'bg-[var(--haste-yellow)] text-black hover:bg-[#ffcc00] active:scale-[0.98]',
        destructive: 'bg-red-600 text-white hover:bg-red-700',
        outline: 'border-2 border-[var(--haste-yellow)] text-[var(--haste-yellow)] bg-transparent hover:bg-[var(--haste-yellow)] hover:text-black',
        secondary: 'bg-gray-700 text-white hover:bg-gray-600',
        ghost: 'hover:bg-gray-800 hover:text-[var(--haste-yellow)]',
        link: 'text-[var(--haste-yellow)] underline-offset-4 hover:underline',
      },
      size: {
        default: 'h-10 px-4 py-2',
        sm: 'h-9 rounded-md px-3',
        lg: 'h-12 rounded-md px-8 text-base',
        icon: 'h-10 w-10',
      },
    },
    defaultVariants: {
      variant: 'default',
      size: 'default',
    },
  }
);
</script>

