<script>
    import { username  } from "./stores";

    let user = '';
    let password = '';
  
    function handleSubmit() {

      console.log('Username:', user);
      username.set(user);

    }
  </script>

<main>
    <form on:submit|preventDefault={handleSubmit}>
      <table>
        <thead>
          <tr>
            <th>Username:</th>
            <th>Password:</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><input type="text" bind:value={ user } /></td>
            <td><input type="password" bind:value={password} /></td>
          </tr>
          <tr>
            <td colspan="2">
              <button type="submit">Login</button>
            </td>
          </tr>
        </tbody>
      </table>
    </form>
  </main>

  <style>
    /* Table */
    table {
      width: 100%;
      border-collapse: collapse;
    }
  
    /* Table Head */
    thead {
      background-color: #333;
      color: #fff;
    }
  
    thead th {
      padding: 10px;
      text-align: left;
      border-bottom: 1px solid #555;
    }
  
    /* Table Body */
    tbody {
      background-color: #222;
    }
  
    tbody td {
      padding: 10px;
      border-bottom: 1px solid #555;
      color: #fff;
    }
  
    /* Alternate row color */
    tbody tr:nth-child(even) {
      background-color: #333;
    }
  
    /* Username and Password inputs */
    input[type="text"],
    input[type="password"] {
      padding: 10px;
      width: 100%;
      box-sizing: border-box;
      border: 1px solid #555;
      background-color: #333;
      color: #fff;
      border-radius: 4px;
      outline: none;
    }
  
    /* Style for focused text boxes */
    input[type="text"]:focus,
    input[type="password"]:focus {
      border-color: #777;
    }
  
    /* Button */
    button {
      padding: 5px 10px;
      background-color: #555;
      border: none;
      color: #fff;
      cursor: pointer;
      display: inline-block;
      vertical-align: middle;
    }
  
    button:hover {
      background-color: #777;
    }
  
    /* Center the login form */
    main {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
  
    /* Additional styles for the login form */
    form {
      width: 100%;
      max-width: 400px; /* Adjust the maximum width as desired */
      padding: 20px;
      margin: 0 auto;
      background-color: #222;
      border-radius: 4px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    }
  
    /* Style the table within the form */
    form table {
      width: 100%;
    }
  
    /* Remove default form styles */
    form input[type="text"],
    form input[type="password"] {
      border: none;
      outline: none;
      background-color: transparent;
      color: #fff;
      outline: auto;
    }
  
    form button {
      width: 100%;
      margin-top: 20px;
    }
  </style>
  