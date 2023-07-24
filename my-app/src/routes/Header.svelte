<script>
    import {currentDisplay, username} from "./stores.js" 
    let user = "";


    function logout() {
      username.set("");
    }

    function handleClick(index) {

      if (index == 4) {
        logout();
        return;
      }
      currentDisplay.set(index);
  }

  username.subscribe((username) => {
    user = username;
	});
  


</script>


<header class="bg-teal-500 h-16 flex justify-center items-center px-4 ">
  <nav class="flex items-center space-x-4 ">
    <button class="px-4 py-2 bg-teal-600 text-white rounded-l-lg hover:bg-teal-700" on:click={() => handleClick(0)}>Vote</button>
    <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700" on:click={() => handleClick(2)}>Past Ballots</button>
    <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700" on:click={() => handleClick(1)}>Results</button>
    <button class="px-4 py-2 bg-teal-600 text-white rounded-r-lg hover:bg-teal-700" on:click={() => handleClick(3)}>Login</button>
  </nav>
  {#if user != ""}
  <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700 rounded-lg absolute right-2" on:click={() => handleClick(4)}>{user}</button>
  {/if}
</header>
