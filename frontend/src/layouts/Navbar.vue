<!-- src/components/Navbar.vue -->
<template>
  <nav class="bg-gray-800 p-4">
    <ul class="flex space-x-4">
      <li v-for="route in navLinks" :key="route.path">
        <router-link
            :to="route.path"
            :class="[route.current ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white', 'inline-flex items-center rounded-md px-3 py-2 text-sm font-medium']"
            :aria-current="route.current ? 'page' : undefined"
        >
          {{ route.name }}
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<script setup>
import {useNavLinks} from '@/composables/useNavLinks';

const {navLinks} = useNavLinks();
</script>
