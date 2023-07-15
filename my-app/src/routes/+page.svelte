<script>
  import Header from "./Header.svelte";
  import CompletedBallots from "./CompletedBallots.svelte";
  import Voting from "./Voting.svelte";
  import Results from "./Results.svelte";
  import Login from "./Login.svelte"
  import {voted, results, currentDisplay} from "./stores.js";
  let display;

  // display values:
  // 0 = vote, 1 = results, 2 = past ballots

	voted.subscribe((voted) => {
    display ? display = 0 : display = 1;
	});

  currentDisplay.subscribe((currentDisplay) => {
		display = currentDisplay;
	});



</script>
<Header />

<main>
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

<style>
  :global(body) {
    background-color: #111;
  }

  main {
  margin-top: 10px; /* Adjust this value to create space below the header */
  padding: 20px;
  }

</style>