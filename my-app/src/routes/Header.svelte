<script>
    import {currentDisplay, username} from "./stores.js" 

       let user = "";
       let dropDown = false;


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


  <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700 rounded-lg absolute right-2" on:click={() => dropDown = !dropDown}>{user}</button>
  {#if dropDown}
  <ul class="absolute top-16 right-4 bg-teal-600 text-white rounded-lg shadow-md">
    <li class="hover:bg-teal-700">
      <a href="#" class="block px-4 py-3">Change Password</a>
    </li>
    <li class="hover:bg-teal-700">
      <a href="#" class="block px-4 py-3">Logout</a>
    </li>
  </ul>
  {/if}




  <!-- {#if user != ""}
  <button class="px-4 py-2 bg-teal-600 text-white hover:bg-teal-700 rounded-lg absolute right-2" on:click={() => handleClick(4)}>{user}</button>
  {/if} -->
</header>
