// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from "../views/Home.vue";

const routes = [
    {
        path: '/',
        name: 'Home',
        component:  Home,
        meta: {showInNav: false, requiresAuth: false}
    },
    {
        path: '/products',
        name: 'Home',
        component:  () => import('@/views/Products.vue'),
        meta: {showInNav: true, requiresAuth: false}
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
