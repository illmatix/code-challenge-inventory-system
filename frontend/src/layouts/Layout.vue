<template>
  <Disclosure as="header" class="bg-gray-800" v-slot="{ open }">
    <div class="mx-auto max-w-7xl px-2 sm:px-4 lg:divide-y lg:divide-gray-700 lg:px-8">
      <div class="relative flex h-16 justify-between">
        <div class="relative z-10 flex px-2 lg:px-0">
          <div class="flex shrink-0 items-center">
            <RouterLink to="/"><Icon name="BuildingStorefrontIcon" variant="outline" class="text-gray-400 h-8 w-8"></Icon></RouterLink>
          </div>
        </div>
        <div class="relative z-0 flex flex-1 items-center justify-center px-2 sm:absolute sm:inset-0">
          <Search></Search>
        </div>

        <div class="relative z-10 flex items-center lg:hidden">
          <MobileMenuButton></MobileMenuButton>
        </div>

        <div class="hidden lg:relative lg:z-10 lg:ml-4 lg:flex lg:items-center">
          <Profile></Profile>
        </div>
      </div>

      <Navbar></Navbar>
    </div>

    <DisclosurePanel as="nav" class="lg:hidden" aria-label="Global">
      <MobileMenu></MobileMenu>
    </DisclosurePanel>
  </Disclosure>

  <main class="bg-white">
    <RouterView></RouterView>
  </main>

</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './Navbar.vue';
import {Disclosure} from '@headlessui/vue';
import Icon from '../components/helpers/Icon.vue';
import Search from "./Search.vue";
import MobileMenu from "./MobileMenu.vue";
import Profile from "./Profile.vue";
import MobileMenuButton from "./MobileMenuButton.vue";
</script>
