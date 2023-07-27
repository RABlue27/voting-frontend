<script>

import { currentDisplay, username } from "./stores.js";
import { onMount } from 'svelte';

let user = "";
let dropDown = false;

onMount(async () => {
		user = localStorage.getItem("username");
	});


function logout() {
  user = "";
  dropDown = false;
  username.set("");
  localStorage.setItem("username", "");

}

function handleClick(index) {
  if (index === 4) {
    logout();
    return;
  }
  currentDisplay.set(index);
}

username.subscribe((value) => {
  user = value;
});

  


</script>


<header class="bg-teal-500 h-16 flex justify-center items-center px-4 ">
  <img class="h-14 absolute left-4" src="https://mlbawards.xyz/logo.png" alt="Logo">
  
  <nav class="flex items-center space-x-4 ">
    {#if user === ""}
    <button class="px-4 py-2 bg-teal-600 text-white rounded-l-lg hover:bg-teal-700" on:click={() => handleClick(0)}>Vote</button>
    <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700" on:click={() => handleClick(2)}>Past Ballots</button>
    <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700" on:click={() => handleClick(1)}>Results</button>
    <button class="px-4 py-2 bg-teal-600 text-white rounded-r-lg hover:bg-teal-700" on:click={() => handleClick(3)}>Login</button>
    {:else}
    <button class="px-4 py-2 bg-teal-600 text-white rounded-l-lg hover:bg-teal-700" on:click={() => handleClick(0)}>Vote</button>
    <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700" on:click={() => handleClick(2)}>Past Ballots</button>
    <button class="px-4 py-2 bg-teal-600 text-white rounded-r-lg hover:bg-teal-700" on:click={() => handleClick(1)}>Results</button>
    {/if}
  </nav>
  {#if user != ""}
  <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700 rounded-lg absolute right-2" on:click={() => dropDown = !dropDown}>{user}</button>
  {/if}
  {#if dropDown}
  <ul class="absolute top-16 right-4 bg-teal-600 text-white rounded-lg shadow-md">
    <li class="hover:bg-teal-700 rounded-lg">
      <button class="block px-4 py-3">Change Password</button>
    </li>
    <li class="hover:bg-teal-700 rounded-lg">
      <button on:click={() => logout()} class="block px-4 py-3">Logout</button>
    </li>
  </ul>
  
  {/if}




  <!-- {#if user != ""}
  <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700 rounded-lg absolute right-2" on:click={() => handleClick(4)}>{user}</button>
  {/if} -->
</header>
