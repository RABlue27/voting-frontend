import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [
    sveltekit(),
    // Other plugins you might have
  ],
  build: {
    rollupOptions: {
      external: ['simple-svelte-autocomplete'],
      // Other rollup options if needed
    },
  },
});
