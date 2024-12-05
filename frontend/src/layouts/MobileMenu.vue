<template>

    <div class="space-y-1 px-2 pb-3 pt-2">
      <DisclosureButton v-for="item in navLinks" :key="item.name" as="a" :href="item.href" :class="[item.current ? 'bg-gray-900 text-white' : 'text-gray-300 hover:bg-gray-700 hover:text-white', 'block rounded-md px-3 py-2 text-base font-medium']" :aria-current="item.current ? 'page' : undefined">{{ item.name }}</DisclosureButton>
    </div>
    <div class="border-t border-gray-700 pb-3 pt-4" :if="isAuthenticated">
      <div class="flex items-center px-4">
        <div class="shrink-0">
          <img class="size-10 rounded-full" :src="user?.imageUrl" alt="" />
        </div>
        <div class="ml-3">
          <div class="text-base font-medium text-white">{{ user?.name }}</div>
          <div class="text-sm font-medium text-gray-400">{{ user?.email }}</div>
        </div>
        <button type="button" class="relative ml-auto shrink-0 rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
          <span class="absolute -inset-1.5" />
          <span class="sr-only">View notifications</span>
          <BellIcon class="size-6" aria-hidden="true" />
        </button>
      </div>
      <div class="mt-3 space-y-1 px-2">
        <DisclosureButton v-for="item in userNavigation" :key="item.name" as="a" :href="item.href" class="block rounded-md px-3 py-2 text-base font-medium text-gray-400 hover:bg-gray-700 hover:text-white">{{ item.name }}</DisclosureButton>
      </div>
    </div>

</template>
<script setup>
import {DisclosureButton} from "@headlessui/vue";

import {useNavLinks} from '@/composables/useNavLinks';
import {useUser} from "@/composables/useUser";

const {navLinks} = useNavLinks();
const {user, isAuthenticated, isAdmin, isManager, logout } = useUser();
</script>