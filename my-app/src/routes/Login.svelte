<script>
    import { username  } from "./stores";

    let user = '';
    let password = '';
  
    function handleSubmit() {

      console.log('Username:', user);
      username.set(user);

    }
  </script>


<form class="max-w-sm mx-auto p-4 bg-white rounded shadow-md" on:submit|preventDefault={handleSubmit}>
  <table class="w-full">
    <thead>
      <tr>
        <th class="py-2">Username:</th>
        <th class="py-2">Password:</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="py-2"><input type="text" class="w-full px-4 py-2 border rounded focus:outline-none focus:ring focus:border-blue-500" bind:value={user} /></td>
        <td class="py-2"><input type="password" class="w-full px-4 py-2 border rounded focus:outline-none focus:ring focus:border-blue-500" bind:value={password} /></td>
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
