<template>
  <component
      :is="icon"
      :class="computedClass"
      v-bind="attrs"
  />
</template>

<script setup>
import {computed, toRefs, useAttrs} from 'vue';
// Import all Heroicons
import * as HeroiconsSolid from '@heroicons/vue/24/solid';
import * as HeroiconsOutline from '@heroicons/vue/24/outline';

const props = defineProps({
  name: {
    type: String,
    required: true,
    // Example: "HomeIcon" (case-sensitive)
  },
  variant: {
    type: String,
    default: 'solid',
    // Options: "solid" or "outline"
  },
  size: {
    type: [String, Number],
    default: 24,
    // Size in pixels
  },
  class: {
    type: String,
    default: '',
    // Additional Tailwind classes
  },
});

const { name, variant, size } = toRefs(props);

// Resolve the icon dynamically based on the variant
const icon = computed(() => {
  const icons =
      variant.value === 'outline' ? HeroiconsOutline : HeroiconsSolid;
  return icons[name.value] || null;
});

// Add size and any extra Tailwind classes
const computedClass = computed(() => `${props.class} h-${size.value} w-${size.value}`);

// Capture any additional attributes passed to the component
const attrs = useAttrs();
</script>
