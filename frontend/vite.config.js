import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/home': 'http://127.0.0.1:8000', //* this allows for the backend & front end to communicate w/ each other
    },
  },
})
