import { writable } from 'svelte/store';

export const voted = writable(false);

export const currentDisplay = writable(0);

export const results = writable([]);

export const username = writable("");