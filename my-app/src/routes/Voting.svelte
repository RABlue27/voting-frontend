<script>
    import { onMount } from 'svelte';
    import AutoComplete from "simple-svelte-autocomplete"
  
    let players = ["", "", "", ""];
    let comments = ["", "", "", ""];
    let votes = [false, false, false, false];
    let didv;
    let user = "";
    const allPlayers = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua &amp; Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia &amp; Herzegovina","Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Estonia","Ethiopia","Falkland Islands","Faroe Islands","Fiji","Finland","France","French Polynesia","French West Indies","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guam","Guatemala","Guernsey","Guinea","Guinea Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kuwait","Kyrgyz Republic","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Macau","Macedonia","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Mauritania","Mauritius","Mexico","Moldova","Monaco","Mongolia","Montenegro","Montserrat","Morocco","Mozambique","Namibia","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Norway","Oman","Pakistan","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russia","Rwanda","Saint Pierre &amp; Miquelon","Samoa","San Marino","Satellite","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","South Africa","South Korea","Spain","Sri Lanka","St Kitts &amp; Nevis","St Lucia","St Vincent","St. Lucia","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad &amp; Tobago","Tunisia","Turkey","Turkmenistan","Turks &amp; Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"];
    import { voted, currentDisplay, results, username } from "./stores.js";

	voted.subscribe((voted) => {
    voted ? didv = true: didv = false;
	});

	username.subscribe((username) => {
    user = username;
	});
  


    function saveVotingData() {
      localStorage.setItem('votingData', JSON.stringify({ players, comments, votes }));
    }

    function jsonifyVotes(){
      var j = {};
      for (let i = 0; i < players.length; i++) {
        let playerKey = "player" + (i + 1);
        let commentKey = "comment" + (i + 1);
        
        j[playerKey] = players[i];
        j[commentKey] = comments[i];
}
      j.user = user;
      j.timestamp = Date.now();
      return j;
    }

    import { fade } from 'svelte/transition';
  
    function postVotesToBackend() {
      let results = jsonifyVotes();
      console.log(results);
      // results.set(players.filter((player, index) => votes[index] !== false));
      votes = votes.map(() => true);
      // voted.set(true);
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
      // comments[index] = event.target.value;
      return;
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
        voted.set = false;
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

  <!-- <input type="text" disabled={votes[index]} bind:value={players[index]} on:input={(e) => handleChange(e, index)} /> -->

  <AutoComplete
  items="{allPlayers}"
  placeholder={players[index]}
  bind:value={players[index]}
  hideArrow={true}
  disabled={votes[index]}
/>

  <input type="text" disabled={votes[index]} bind:value={comments[index]}/>
  <button on:click={() => { handleVote(index); handleComment(index); }}>{votes[index] ? "Undo Vote" : "Save Vote"}</button>
  
  {/each}
  
  
  <button on:click={() => { postVotesToBackend() }} class="finalize-votes">Finalize and Submit Votes</button> 
  <button on:click={() => { resetAll()  }}>Reset Everything</button>

  <style>
    .container {
      background-color: #1a1a1a;
      padding: 10px;
      margin-bottom: 10px;
      border-radius: 4px;
      box-shadow: 0 2px 4px rgba(255, 255, 255, 0.1);
    }
  
    .container:disabled {
    opacity: 0.5;
    pointer-events: none;
    background-color: #888888;
    cursor: not-allowed;
    border: 2px solid red;
}



h1, h2 {
  display: inline;
}

    h1 {
      font-size: 20px;
      font-weight: bold;
      color: #fff;
      margin-bottom: 5px;
    }
  
    h2 {
      font-size: 16px;
      font-weight: bold;
      color: #fff;
      margin-bottom: 5px;
    }
  
    input[type="text"] {
      font-family: 'Arial', sans-serif;
      font-size: 14px;
      color: #fff;
      background-color: #333;
      padding: 8px;
      border: 1px solid #444;
      border-radius: 4px;
      margin-bottom: 10px;
    }
  
    input[type="text"]:disabled {
      opacity: 0.5;
    cursor: not-allowed;
    background-color: #888888;
    }

    button {
      font-family: 'Arial', sans-serif;
      font-size: 14px;
      color: #fff;
      background-color: #007bff;
      border: none;
      border-radius: 4px;
      padding: 8px 16px;
      cursor: pointer;
    }
  
    .finalize-votes {
      background-color: #dc3545;
      margin-right: 10px;
    }
  
    button:focus {
      outline: none;
    }
  
    button:disabled {
      background-color: #777;
      cursor: not-allowed;
    }
  
    .container:last-child {
      margin-bottom: 0;
    }



  </style>