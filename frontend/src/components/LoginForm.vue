<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <input v-model="credentials.username" placeholder="Username" />
      <input v-model="credentials.password" type="password" placeholder="Password" />
      <button type="submit">Login</button>
    </form>
    <div v-if="error" class="text-red-500">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/authStore';

const authStore = useAuthStore();
const credentials = ref({ username: '', password: '' });
const { error, login } = authStore;

const submitLogin = () => login(credentials.value);
</script>
