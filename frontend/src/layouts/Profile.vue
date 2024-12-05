<template>
  <template v-if="isAuthenticated">
    <button type="button" class="relative shrink-0 rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
      <span class="absolute -inset-1.5" />
      <span class="sr-only">View notifications</span>
      <BellIcon class="size-6" aria-hidden="true" />
    </button>

    <div class="relative ml-4 shrink-0">
      <Menu as="div">
        <MenuButton
            class="relative flex rounded-full bg-gray-800 text-sm text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800"
        >
          <span class="absolute -inset-1.5" />
          <span class="sr-only">Open user menu</span>
          <img class="size-8 rounded-full" :src="user.imageUrl" alt="User profile image" />
        </MenuButton>
        <transition
            enter-active-class="transition ease-out duration-100"
            enter-from-class="transform opacity-0 scale-95"
            enter-to-class="transform opacity-100 scale-100"
            leave-active-class="transition ease-in duration-75"
            leave-from-class="transform opacity-100 scale-100"
            leave-to-class="transform opacity-0 scale-95"
        >
          <MenuItems class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black/5 focus:outline-none">
            <MenuItem v-for="item in userNavigation" :key="item.name" v-slot="{ active }">
              <a
                  :href="item.href"
                  :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']"
              >
                {{ item.name }}
              </a>
            </MenuItem>
          </MenuItems>
        </transition>
      </Menu>
    </div>
  </template>
  <template v-else>
    <button class="text-gray-300 hover:bg-gray-700 hover:text-white inline-flex items-center rounded-md px-3 py-2 text-sm font-medium">Login</button>
  </template>
</template>


<script setup>
import {useUser} from "@/composables/useUser";
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';

const {user, isAuthenticated, isAdmin, isManager, logout } = useUser();

const userNavigation = [
  { name: 'Your Profile', href: '/me' },
  { name: 'Settings', href: '/settings' },
  { name: 'Sign out', href: '/logout' },
];

</script>
