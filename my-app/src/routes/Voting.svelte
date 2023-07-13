<script>
    import { onMount } from 'svelte';
  
    let players = ["", "", "", ""];
    let comments = ["", "", "", ""];
    let votes = [false, false, false, false];
    let didv;
    import { voted, currentDisplay, results } from "./stores.js";

	voted.subscribe((voted) => {
    voted ? didv = true: didv = false;
	});

  
    function saveVotingData() {
      localStorage.setItem('votingData', JSON.stringify({ players, comments, votes }));
    }
  
    function submitVotes() {
      results.set(players.filter((player, index) => votes[index] !== false));
      voted.set(true);
      currentDisplay.set(1);
      saveVotingData();
    }

    onMount(() => {
      const storedData = localStorage.getItem('votingData');
      if (storedData) {
        const { players: storedPlayers, comments: storedComments, votes: storedVotes } = JSON.parse(storedData);
        players = storedPlayers;
        comments = storedComments;
        votes = storedVotes;
      }
    });
  
    function handleChange(event, index) {
      players[index] = event.target.value;
    }
  
    function handleComment(event, index) {
      comments[index] = event.target.value;
    }
  
    function handleVote(index) {
      players[index] = players[index];
      votes[index] = !votes[index];
      saveVotingData();
    }
  
    function subject(index) {
      const categories = ['AL hitter', 'AL pitcher', 'NL hitter', 'NL pitcher'];
      return categories[index];
    }

    function resetAll() {
        players = ["", "", "", ""];
        comments = ["", "", "", ""];
        votes = [false, false, false, false];
        localStorage.removeItem('votingData');
}

  </script>
  


{#each players as player, index}
  <div class="container">
    {#if player != "" && votes[index] != false}
    <h1>You Voted For: </h1>
    <h2>{player}</h2>
    {:else}
    <h1> Vote for {subject(index)} </h1>
    {/if}
  </div>

  <input type="text" disabled={votes[index]} bind:value={players[index]} on:input={(e) => handleChange(e, index)} />
  <input type="text" disabled={votes[index]} bind:value={comments[index]} on:input={(e) => handleComment(e, index)} />
  <button on:click={() => { handleVote(index); handleComment(index); }}>{votes[index] ? "Undo Vote" : "Save Vote"}</button>
  
  {/each}
  
  
  <button on:click={() => { submitVotes() }} class="finalize-votes">Finalize and Submit Votes</button> 
  <button on:click={() => { resetAll()  }}>Reset Everything</button>

  <style>
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
  
    /* Container */
    .container {
      margin-bottom: 20px;
    }
  
    .container h1 {
      font-size: 24px;
      margin-bottom: 10px;
      color: #fff;
    }
  
    .container h2 {
      font-size: 18px;
      color: #fff;
    }
  
    /* Inputs */
    input[type="text"] {
      padding: 5px;
      width: 100%;
      box-sizing: border-box;
      border: 1px solid #555;
      background-color: #333;
      color: #fff;
      border-radius: 4px;
      outline: none;
    }
  
    /* Disabled Inputs */
    input[type="text"]:disabled {
      background-color: #555;
      cursor: not-allowed;
    }
  
    button.finalize-votes {
    margin-top: 20px;
    background-color:green;
    border: none;
    color: #fff;
    padding: 15px 30px;
    cursor: pointer;
    display: inline-block;
    vertical-align: middle;
    font-size: 20px; 
    font-weight: bold;
    border-radius: 4px; 
  }

  button.finalize-votes:hover {
    background-color: #777;
  }
  </style>
  