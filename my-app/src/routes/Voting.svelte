<script>
    import {
        onMount
    } from 'svelte';
    import AutoComplete from "simple-svelte-autocomplete"
    import { playersList } from './playerList';
    
    let players = ["", "", "", ""];
    let comments = ["", "", "", ""];
    let votes = [false, false, false, false];
    
    let mplayers = ["", "", "", ""];
    let mcomments = ["", "", "", ""];
    let mvotes = [false, false, false, false];
    
    let didv;
    let user = "";
    let isMonthly = true;
    const allPlayers = playersList
    import {
        voted,
        currentDisplay,
        username,
        results
    } from "./stores.js";
    
    voted.subscribe((voted) => {
        voted ? didv = true : didv = false;
    });
    
    username.subscribe((username) => {
        user = username;
    });
    
    
    
    function saveVotingData() {
        localStorage.setItem('votingData', JSON.stringify({
            players,
            comments,
            votes
        }));
        localStorage.setItem('monthlyData', JSON.stringify({
            mplayers,
            mcomments,
            mvotes
        }));
    }
    
    function jsonifyVotes() {
        var j = {};
        for (let i = 0; i < players.length; i++) {
            let playerKey = "player" + (i + 1);
            let commentKey = "comment" + (i + 1);
    
            j[playerKey] = players[i];
            j[commentKey] = comments[i];
        }
        j.user = localStorage.getItem("username");
        j.timestamp = Date.now();
        j.isMonthly = false;
        return j;
    }
    
    function jsonifyMonthly() {
        var j = {};
        for (let i = 0; i < mplayers.length; i++) {
            let playerKey = "player" + (i + 1);
            let commentKey = "comment" + (i + 1);
    
            j[playerKey] = mplayers[i];
            j[commentKey] = mcomments[i];
        }
        j.user = localStorage.getItem("username");
        j.timestamp = Date.now();
        j.isMonthly = true;
        return j;
    }
    
    function postVotesToBackend() {
    
        let results = jsonifyVotes();
        if (isMonthly) { let m = jsonifyMonthly(); console.log(m); mvotes = mvotes.map(() => true); }
        console.log(results);
        votes = votes.map(() => true);
        currentDisplay.set(1);
        saveVotingData();
    }
    
    onMount(() => {
        const storedData = localStorage.getItem('votingData');
        if (storedData) {
            const {
                players: storedPlayers,
                comments: storedComments,
                votes: storedVotes
            } = JSON.parse(storedData);
            players = storedPlayers;
            comments = storedComments;
            votes = storedVotes;
        }
        if (isMonthly) {
            const secondData = localStorage.getItem('monthlyData');
            if (secondData) {
            const {
                mplayers: storedPlayers,
                mcomments: storedComments,
                mvotes: storedVotes
            } = JSON.parse(secondData);
            mplayers = storedPlayers;
            mcomments = storedComments;
            mvotes = storedVotes;
        }
        }
    });
    
    function handleChange(event, index) {
        players[index] = event.target.value;
    }
    
    function handleComment(event, index, isMonth) {
        // comments[index] = event.target.value;
        return;
    }
    
    function handleVote(index, isMonth) {
        if (!isMonth) {
        players[index] = players[index];
        votes[index] = !votes[index];
        saveVotingData();
        return;
        }  
        mplayers[index] = mplayers[index];
        mvotes[index] = !mvotes[index];
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
        mplayers = ["", "", "", ""];
        mcomments = ["", "", "", ""];
        mvotes = [false, false, false, false];
        localStorage.removeItem('monthlyData');
    }
    
    function handleCreate(player) {
    
        return player;
    
    }
    
    function getNdaysFanduel(level, type, n) {
        const currentDate = new Date();
        currentDate.setDate(currentDate.getDate() - 1);
        const lastWeekDate = new Date(currentDate.getTime() - n * 24 * 60 * 60 * 1000);
    
        const currentYear = currentDate.getFullYear();
        const currentMonth = String(currentDate.getMonth() + 1).padStart(2, '0');
        const currentDay = String(currentDate.getDate()).padStart(2, '0');
    
        const lastWeekYear = lastWeekDate.getFullYear();
        const lastWeekMonth = String(lastWeekDate.getMonth() + 1).padStart(2, '0');
        const lastWeekDay = String(lastWeekDate.getDate()).padStart(2, '0');
    
    
        // "                              https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=nl&qual=y&type=8&season=2023&month=1000&season1=2023&ind=0&team=0&rost=&age=0&filter=&players=&startdate=2023-07-23&enddate=2023-07-30"
        const modifiedURL = `https://www.fangraphs.com/leaders.aspx?pos=all&stats=${type}&lg=${level}&qual=y&type=8&season=2023&month=1000&season1=2023&ind=0&team=0&rost=&age=0&filter=&players=&startdate=${lastWeekYear}-${lastWeekMonth}-${lastWeekDay}&enddate=${currentYear}-${currentMonth}-${currentDay}`;
        return modifiedURL;
    }
    
    
    function getNdaysBR(level, type, n) {
        const currentDate = new Date();
        const lastWeekDate = new Date(currentDate.getTime() - 7 * 24 * 60 * 60 * 1000);
    
        const modifiedURL = `https://www.baseball-reference.com/leagues/daily.fcgi?request=1&type=${type}&user_team=&bust_cache=&dates=lastndays&lastndays=${n}&level=${level}&franch=ANY`;
        return modifiedURL;
    }
    
    // AL hitter, AL pitcher, NL hitter, NL pitcher
    function fangraphsClick(i, d) {
        switch (i) {
            case 0:
                window.open(getNdaysFanduel("al", "bat", d));
                return;
            case 1:
                window.open(getNdaysFanduel("al", "pit", d));
                return;
            case 2:
                window.open(getNdaysFanduel("nl", "bat", d));
                return;
            case 3:
                window.open(getNdaysFanduel("nl", "pit", d));
                return;
            default:
                console.log("Disaster");
        }
    }
    
    function brClick(i, d) {
        switch (i) {
            case 0:
                window.open(getNdaysBR("mlb-al", "b", d));
                return;
            case 1:
                window.open(getNdaysBR("mlb-al", "p", d));
                return;
            case 2:
                window.open(getNdaysBR("mlb-nl", "b", d));
                return;
            case 3:
                window.open(getNdaysBR("mlb-nl", "p", d));
                return;
            default:
                console.log("Disaster");
        }
    }



      </script>
      
      <p class="text-5xl mb-4">Open Ballots</p>
    
      <div class="bg-gray-200 pr-8 pl-8 pb-8 pt-2 w-4/12 rounded-md">
        {#each players as player, index}
        <div class="flex items-center">
          {#if player && votes[index]}
          <h1 class="text-3xl mt-2.5 font-semibold underline ml-2">You Voted For: {player}</h1>
          {:else}
          <h1 class="text-3xl mt-2.5 font-semibold underline ml-2"> Vote for {subject(index)}</h1>
          <div class="ml-auto"> 
            <div class="flex space-x-1 mt-2 mb-1 bg-gray-200 p-1 mr-2">
    
              <button on:click={() => fangraphsClick(index, 7)} class="bg-green-500 hover:bg-green-600 px-4 py-2 rounded-sm text-white h-10 flex items-center cursor-pointer">FG Stats</button>
              <button on:click={() => brClick(index, 7)}  class="bg-red-400 hover:bg-red-500 px-4 py-2 rounded-sm text-white h-10 flex items-center cursor-pointer">BR Stats</button>
    
            </div>
          </div>
          {/if}
        </div>
        
        <div class="flex flex-col space-y-4 m-2 ">
    
          <AutoComplete
            items="{allPlayers}"
            placeholder={players[index]}
            bind:value={players[index]}
            hideArrow={true}
            disabled={votes[index]}
            create={true}
            onCreate={handleCreate}
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
      on:click={() => { handleVote(index, false); handleComment(index, false); }}
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
    
    
    {#if isMonthly} 
    <p class="text-5xl mb-4">Monthly Ballots</p>
    
      <div class="bg-gray-200 pr-8 pl-8 pb-8 pt-2 w-4/12 rounded-md">
        {#each mplayers as player, index}
        <div class="flex items-center">
          {#if player && mvotes[index]}
          <h1 class="text-3xl mt-2.5 font-semibold underline ml-2">You Voted For: {player}</h1>
          {:else}
          <h1 class="text-3xl mt-2.5 font-semibold underline ml-2"> Vote for {subject(index)}</h1>
          <div class="ml-auto"> 
            <div class="flex space-x-1 mt-2 mb-1 bg-gray-200 p-1 mr-2">
    
              <button on:click={() => fangraphsClick(index, 30)} class="bg-green-500 hover:bg-green-600 px-4 py-2 rounded-sm text-white h-10 flex items-center cursor-pointer">FG Stats</button>
              <button on:click={() => brClick(index, 30)}  class="bg-red-400 hover:bg-red-500 px-4 py-2 rounded-sm text-white h-10 flex items-center cursor-pointer">BR Stats</button>
    
            </div>
          </div>
          {/if}
        </div>
        
        <div class="flex flex-col space-y-4 m-2 ">
    
          <AutoComplete
            items="{allPlayers}"
            placeholder={mplayers[index]}
            bind:value={mplayers[index]}
            hideArrow={true}
            disabled={mvotes[index]}
            create={true}
            onCreate={handleCreate}
            class="px-1 p-2 rounded-sm border disabled:bg-slate-200 w-full placeholder-black border-stone-950"
          />
        
          <textarea 
            type="text" 
            disabled={mvotes[index]} 
            bind:value={mcomments[index]} 
            placeholder="Comments (Optional)"
            class="px-1 py-2 rounded-sm border disabled:bg-slate-200 w-full border-stone-950 resize-y"
          ></textarea>
        </div>
        
    
    
      <button 
      on:click={() => { handleVote(index, true); handleComment(index, true); }}
      class={
        `ml-2 mt-1 py-2 px-4 mb-2 bg-teal-500 hover:bg-teal-600 focus:bg-teal-700 text-white font-medium rounded-lg shadow-md ${
          mvotes[index] ? 'dark:bg-teal-700' : ''
        }`}>
      {mvotes[index] ? "Undo Vote" : "Save Vote"}
    </button>
      {/each}
    
      
    </div>
    {/if}
    <div class="flex space-x-10 items-center">
      <button on:click={() => { postVotesToBackend() }} class="my-4 py-2 px-4 bg-green-700 hover:bg-green-900 text-white text-4xl font-semibold rounded h-20 w-64">Submit</button> 
      <button on:click={() => { resetAll() }} class="my-4 py-2 px-4 bg-red-700 hover:bg-rose-900 text-white font-semibold text-4xl rounded w-64 h-20">Reset</button>
    </div>


    <p> Toggle Monthly Status </p>
    <input type="checkbox" class="form-checkbox h-5 w-5 text-indigo-600 mb-12" bind:checked={isMonthly}>
