<!-- MobileMenu.vue -->
<template>
    <!-- Mobile menu button -->
    <DisclosureButton class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white">
      <span class="absolute -inset-0.5" />
      <span class="sr-only">Open menu</span>
      <Bars3Icon v-if="!open" class="block size-6" aria-hidden="true" />
      <XMarkIcon v-else class="block size-6" aria-hidden="true" />
    </DisclosureButton>
</template>
