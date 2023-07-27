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


function fangraphsClick(i) {
  window.open("https://www.fangraphs.com/");
}
function brClick(i) {
  window.open("https://www.baseball-reference.com/");

}

function getUrlsAttribute() {
    if (this.slug !== null) {
        let urls = [];
        let exp = this.slug.split('-');
        let start = this.start;
        let end = this.stop;

        let league = exp[0];
        let type = exp[1];

        ['fg', 'br'].forEach(brand => {
            if (brand === 'br') {
                if (type === 'bat') {
                    type = 'b';
                } else if (type === 'pitch') {
                    type = 'p';
                }
                urls[brand] = `https://www.baseball-reference.com/leagues/daily.fcgi?request=1&type=${type}&lastndays=7&since=${start}&dates=fromandto&fromandto=${start}.${end}&level=mlb-${league}&franch=ANY&stat_value=0`;
            } else if (brand === 'fg') {
                if (type === 'bat') {
                    type = 'bat';
                } else if (type === 'pitch') {
                    type = 'pit';
                }
                urls[brand] = `https://www.fangraphs.com/leaders.aspx?pos=all&stats=${type}&lg=${league}&qual=y&type=8&season=2020&month=1000&season1=2020&ind=0&team=0&rost=0&age=0&filter=&players=0&startdate=${start}&enddate=${end}`;
            }
        });
        console.log(urls);
        return urls;
    } else {
        return null;
    }

}

  </script>
  
  <p class="text-5xl mb-4">Open Ballots</p>
  <div class="bg-gray-200 pr-8 pl-8 pb-8 pt-2 w-4/12 rounded-md">
    {#each players as player, index}
    <div class="flex items-center border-b-2">
      {#if player && votes[index]}
      <h1 class="text-3xl mt-2.5 font-semibold underline ml-2">You Voted For: {player}</h1>
      {:else}
      <h1 class="text-3xl mt-2.5 font-semibold underline ml-2"> Vote for {subject(index)}</h1>
      <div class="ml-auto"> 
        <div class="flex space-x-1 mt-2 mb-1 bg-gray-200 p-1 mr-2">

          <button on:click={() => getUrlsAttribute()} class="bg-green-500 hover:bg-green-600 px-4 py-2 rounded-sm text-white h-10 flex items-center cursor-pointer">FG Stats</button>
          <button on:click={() => brClick(index)}  class="bg-red-400 hover:bg-red-500 px-4 py-2 rounded-sm text-white h-10 flex items-center cursor-pointer">BR Stats</button>

        </div>
      </div>
      {/if}
    </div>
    
    <div class="flex flex-col space-y-4 m-2">

      <AutoComplete
        items="{allPlayers}"
        placeholder={players[index]}
        bind:value={players[index]}
        hideArrow={true}
        disabled={votes[index]}
        class="px-1 p-2 rounded-sm border disabled:bg-slate-200 w-full placeholder-black border-stone-950"
      />
    
      <textarea 
        type="text" 
        disabled={votes[index]} 
        bind:value={comments[index]} 
        placeholder="Comments (Optional)"
        class="px-1 py-2 rounded-sm border disabled:bg-slate-200 w-full border-stone-950 resize-y"
      ></textarea>
    </div>
    


  <button 
  on:click={() => { handleVote(index); handleComment(index); }}
  class={
    `ml-2 mt-1 py-2 px-4 mb-2 bg-teal-500 hover:bg-teal-600 focus:bg-teal-700 text-white font-medium rounded-lg shadow-md ${
      votes[index] ? 'dark:bg-teal-700' : ''
    }`
  }
>
  {votes[index] ? "Undo Vote" : "Save Vote"}
</button>
  {/each}
  
</div>
  <div class="flex space-x-10 items-center">
    <button on:click={() => { postVotesToBackend() }} class="my-4 py-2 px-4 bg-green-700 hover:bg-green-900 text-white text-4xl font-semibold rounded h-20 w-64">Submit</button> 
    <button on:click={() => { resetAll() }} class="my-4 py-2 px-4 bg-red-700 hover:bg-rose-900 text-white font-semibold text-4xl rounded w-64 h-20">Reset</button>
  </div>