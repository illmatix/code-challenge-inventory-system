<template>
  <div class="grid w-full grid-cols-1 sm:max-w-xs">
    <input type="search" name="search" aria-label="Search"
           class="col-start-1 row-start-1 block w-full rounded-md bg-gray-700 py-1.5 pl-10 pr-3 text-base text-white outline-none placeholder:text-gray-400 focus:bg-white focus:text-gray-900 focus:placeholder:text-gray-400 sm:text-sm/6"
           placeholder="Search"/>
    <MagnifyingGlassIcon class="pointer-events-none col-start-1 row-start-1 ml-3 size-5 self-center text-gray-400"
                         aria-hidden="true"/>
  </div>
</template>

<script setup>
import {MagnifyingGlassIcon} from '@heroicons/vue/20/solid';
</script>
