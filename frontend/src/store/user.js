import { defineStore } from 'pinia';
import axiosInstance from '@/api/axios';

export const useUserStore = defineStore('userStore', {
    state: () => ({
        users: [],
        loading: false,
        error: null,
    }),

    actions: {
        async fetchUsers() {
            this.loading = true;
            this.error = null;
            try {
                const response = await axiosInstance.get('/users');
                this.users = response.data;
            } catch (err) {
                this.error = err.response?.data?.message || 'Failed to fetch users.';
            } finally {
                this.loading = false;
            }
        },

        async createUser(user) {
            try {
                const response = await axiosInstance.post('/users', user);
                this.users.push(response.data);
            } catch (err) {
                this.error = err.response?.data?.message || 'Failed to create user.';
            }
        },
    },
});
