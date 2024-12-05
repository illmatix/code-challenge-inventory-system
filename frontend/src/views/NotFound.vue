<!-- src/views/NotFound.vue -->
<template>
  <template>
    <div class="py-10">
      <header>
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <h1 class="text-3xl font-bold tracking-tight text-gray-900">404 - Page Not Found</h1>
        </div>
      </header>
      <main>
        <div class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
          <p class="text-gray-700 dark:text-gray-300 mt-2">
            Sorry, the page you are looking for does not exist.
          </p>
          <router-link to="/" class="text-blue-500 hover:underline">Go back to Home</router-link>
        </div>
      </main>
    </div>
  </template>
</template>

<script setup>
// No additional script needed
</script>
