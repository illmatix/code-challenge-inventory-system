import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path';

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    host: '0.0.0.0',
    port: 5173,
    watch: {
      usePolling: true, // Use polling if you're running Vite in Docker or WSL
    },
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
      },
      '/swagger.yaml': {
        target: 'http://localhost:5000',
        changeOrigin: true,
      },
      '/swagger-ui/': {
        target: 'http://localhost:5000',
        changeOrigin: true,
      },
    },
  },
  build: {
    outDir: path.resolve(__dirname, '../public/dist'), // Output Vue files here
    emptyOutDir: true,
  },
  publicDir: path.resolve(__dirname, '../public'),
});
