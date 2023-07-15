<script>
    import {currentDisplay} from "./stores.js" 
    let userName = "RagingAcid";

    function handleClick(index) {
        currentDisplay.set(index);
  }


</script>
<header>
    <button on:click={() => handleClick(0)}>Vote</button>
    <button on:click={() => handleClick(1)}>Results</button>
    <button on:click={() => handleClick(2)}>Past Ballots</button>
    <button on:click={() => handleClick(3)}>Login</button>
    <p> {userName } </p>
</header>



    <style>
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #1a1a1a;
    padding: 10px;
    box-shadow: 0 2px 4px rgba(255, 255, 255, 0.1);
  }

  button {
    font-family: 'Arial', sans-serif;
    font-size: 14px;
    color: #fff;
    background-color: #007bff;
    border: none;
    border-radius: 4px;
    padding: 8px 16px;
    margin-right: 8px;
    cursor: pointer;
  }

  p {
    font-family: 'Arial', sans-serif;
    font-size: 14px;
    color: #fff;
    margin-right: 8px;
  }
    </style>
    