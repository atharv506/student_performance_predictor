import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'https://student-performance-predictor-khzf.onrender.com',
        changeOrigin: true
      }
    }
  }
});
