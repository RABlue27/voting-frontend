<script>
  import Header from "./Header.svelte";
  import CompletedBallots from "./CompletedBallots.svelte";
  import Voting from "./Voting.svelte";
  import Results from "./Results.svelte";
  import Login from "./Login.svelte"
  import {voted, results, currentDisplay} from "./stores.js";
  let display;

	voted.subscribe((voted) => {
    display ? display = 0 : display = 1;
	});

  currentDisplay.subscribe((currentDisplay) => {
		display = currentDisplay;
	});


</script>


<Header /> 

<main class="grid place-items-center h-10/12">
{#if display == 0} 
<Voting bind:results={$results} />
{:else if display == 1} 
<Results />
{:else if display == 2} 
<CompletedBallots />
{:else} 
<Login />
{/if}
</main>

