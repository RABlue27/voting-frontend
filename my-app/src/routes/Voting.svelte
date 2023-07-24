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
  <div>
    {#if player != "" && votes[index] != false}
    <h1 class="text-3xl mt-2.5">You Voted For: {player}</h1>
    {:else}
    <h1 class="text-3xl mt-2.5"> Vote for {subject(index)} </h1>
    {/if}
  </div>


 
  <AutoComplete
  items="{allPlayers}"
  placeholder={players[index]}
  bind:value={players[index]}
  hideArrow={true}
  disabled={votes[index]}
  class="px-1 py-2 rounded-sm border disabled:bg-slate-200 hover:bg-teal-50 w-96 mt-1 placeholder-black border-stone-950"
/>


  <input type="text" disabled={votes[index]} bind:value={comments[index]} class=
  "px-1 py-2 rounded-sm border disabled:bg-slate-200 hover:bg-teal-50 w-96 mb-6 mt-1 border-stone-950" 
  />

  <button 
  on:click={() => { handleVote(index); handleComment(index); }}
  class={
    `py-2 px-4 bg-teal-500 hover:bg-teal-600 focus:bg-teal-700 text-white font-medium rounded shadow ${
      votes[index] ? 'dark:bg-teal-700' : ''
    }`
  }
>
  {votes[index] ? "Undo Vote" : "Save Vote"}
</button>

  
  {/each}
  
  <div class="flex space-x-10">
    <button on:click={() => { postVotesToBackend() }} class="my-4 py-2 px-4 bg-green-700 hover:bg-green-900 text-white font-semibold rounded w-32">Submit Votes</button> 
    <button on:click={() => { resetAll() }} class="my-4 py-2 px-4 bg-red-700 hover:bg-rose-900 text-white font-semibold rounded w-32">Reset Everything</button>
  </div>
  