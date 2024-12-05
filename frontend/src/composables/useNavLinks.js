import { computed } from 'vue';
import { useAuthStore } from '@/store/auth';
import router from '@/router';

export function useNavLinks() {
    const authStore = useAuthStore();

    const navLinks = computed(() => {
        const isAuthenticated = authStore.isAuthenticated;

        return router
            .getRoutes()
            .filter((route) => route.meta.showInNav) // Only show routes marked for navigation
            .filter((route) => {
                if (route.meta.requiresAuth && !isAuthenticated) {
                    return false; // Exclude if user is not authenticated and route requires auth
                }
                return true;
            })
            .map((route) => ({
                name: route.name,
                path: route.path,
            }));
    });

    return { navLinks };
}
