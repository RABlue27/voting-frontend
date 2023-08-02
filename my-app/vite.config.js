import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    sveltekit(),
    // Other plugins you might have
  ],
  build: {
    rollupOptions: {
      // Remove 'simple-svelte-autocomplete' from the 'external' array
      external: [],
      // Other rollup options if needed
    },
  },
});
