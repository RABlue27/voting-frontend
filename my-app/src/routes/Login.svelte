<script>
    import { username } from "./stores";
    let user = '';
    let password = '';
  
    function handleSubmit() { // Actual logic very much needed.

      console.log('Username:', user);
      localStorage.setItem("username", user)
      username.set(user);

    }


  </script>
  
<img class="mt-6" src="https://mlbawards.xyz/logo.png" alt="Logo">

<div class="absolute top-1/3"> 
  <form class="max-w-sm mx-auto p-4 bg-white rounded border-black border-2" on:submit|preventDefault={handleSubmit}>
    <table class="w-full">
      <thead>
        <tr>
          <th class="py-2">Username:</th>
          <th class="py-2">Password:</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="py-2">
            <input
              type="text"
              class="w-full px-4 py-2 border rounded focus:outline-none focus:ring focus:border-blue-500"
              bind:value={user}
              maxlength="20" 
            />
          </td>
          <td class="py-2">
            <input
              type="password"
              class="w-full px-4 py-2 border rounded focus:outline-none focus:ring focus:border-blue-500"
              bind:value={password} maxlength="32"
            />
          </td>
        </tr>
        <tr>
          <td class="py-2" colspan="2">
            <button type="submit" class="w-full bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 focus:outline-none focus:ring focus:border-blue-500">
              Login
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </form>
</div>

