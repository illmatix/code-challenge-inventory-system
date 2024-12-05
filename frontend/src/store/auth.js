import { defineStore } from 'pinia';
import axiosInstance from '@/api/axios';

export const useAuthStore = defineStore('authStore', {
    state: () => ({
        user: null, // Stores user data after login
        token: null, // Stores the JWT token
        error: null, // Stores any errors from API calls
    }),

    getters: {
        // Check if the user is authenticated
        isAuthenticated: (state) => !!state.token,
    },

    actions: {
        // Handle user login
        async login(credentials) {
            try {
                const response = await axiosInstance.post('/auth/login', credentials);
                this.token = response.data.token;
                this.user = response.data.user;

                // Save token in localStorage for persistence
                localStorage.setItem('token', this.token);
                axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
                this.error = null; // Clear previous errors
            } catch (err) {
                this.error = err.response?.data?.message || 'Login failed.';
            }
        },

        // Handle user logout
        logout() {
            this.user = null;
            this.token = null;
            localStorage.removeItem('token');
            delete axiosInstance.defaults.headers.common['Authorization'];
        },

        // Fetch current user data from the backend
        async fetchUser() {
            if (!this.token) return;

            try {
                const response = await axiosInstance.get('/auth/me');
                this.user = response.data.user;
            } catch (err) {
                this.logout(); // Logout if the token is invalid
            }
        },

        // Refresh JWT token
        async refreshToken() {
            try {
                const response = await axiosInstance.post('/auth/refresh');
                this.token = response.data.token;

                // Update token in localStorage and Axios headers
                localStorage.setItem('token', this.token);
                axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
            } catch (err) {
                this.logout(); // Logout if the refresh fails
            }
        },

        // Restore token and user on page reload
        initializeAuth() {
            const token = localStorage.getItem('token');
            if (token) {
                this.token = token;
                axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
                this.fetchUser(); // Fetch user details to populate the state
            }
        },
    },
});
