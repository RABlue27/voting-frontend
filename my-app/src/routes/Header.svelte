<script>
    import {currentDisplay} from "./stores.js" 

    function handleClick(index) {
        currentDisplay.set(index);
  }

</script>

<header>
    <button on:click={() => handleClick(0)}>Vote</button>
    <button on:click={() => handleClick(1)}>Results</button>
    <button on:click={() => handleClick(2)}>Past Ballots</button>
    <button on:click={() => handleClick(3)}>Login</button>
  </header>
  
  <style>
    header {
      background-color: #222;
      display: flex;
      justify-content: center;
      width: 100%;
      position: fixed;
      top: 0;
      left: 0;
    }
  
    /* Buttons */
    button {
      padding: 8px 16px;
      margin: 0 10px;
      background-color: #555;
      color: #fff;
      border: none;
      cursor: pointer;
    }
  
    button:hover {
      background-color: #667;
      color: azure;
    }
  </style>