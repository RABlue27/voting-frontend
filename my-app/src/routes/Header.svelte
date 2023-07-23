<script>
    import {currentDisplay, username} from "./stores.js" 
    let user = "";

    function handleClick(index) {
        currentDisplay.set(index);
  }

  username.subscribe((username) => {
    user = username;
	});
  


</script>


<header class="bg-teal-500 h-16 flex justify-between items-center px-4">
  <nav class="flex items-center space-x-4">
    <button class="px-4 py-2 bg-teal-600 text-white rounded-l-lg hover:bg-teal-700" on:click={() => handleClick(0)}>Vote</button>
    <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700" on:click={() => handleClick(2)}>Past Ballots</button>
    <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700" on:click={() => handleClick(1)}>Results</button>
    <button class="px-4 py-2 bg-teal-600 text-white rounded-r-lg hover:bg-teal-700" on:click={() => handleClick(3)}>Login</button>
  </nav>
  <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700 rounded-lg" on:click={() => handleClick(3)}>{user}</button>
</header>
