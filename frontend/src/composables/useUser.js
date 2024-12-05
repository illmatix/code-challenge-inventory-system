import { computed } from 'vue';
import { useAuthStore } from '@/store/auth';

/**
 * User Composable
 * Provides convenient access to user-related information and actions.
 */
export function useUser() {
    const authStore = useAuthStore();

    // Computed properties to access user information
    const user = computed(() => authStore.user);
    const isAuthenticated = computed(() => authStore.isAuthenticated);
    const isAdmin = computed(() => user.value?.role === 'admin');
    const isManager = computed(() => user.value?.role === 'manager');

    // Logout action
    const logout = () => {
        authStore.logout();
    };

    // Return all utilities
    return {
        user,
        isAuthenticated,
        isAdmin,
        isManager,
        logout,
    };
}
