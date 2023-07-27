<script>
  import Header from "./Header.svelte";
  import CompletedBallots from "./CompletedBallots.svelte";
  import Voting from "./Voting.svelte";
  import Results from "./Results.svelte";
  import Login from "./Login.svelte"
  import {voted, results, currentDisplay, username} from "./stores.js";
  let display;

	voted.subscribe((voted) => {
    display ? display = 0 : display = 1;
	});

  currentDisplay.subscribe((currentDisplay) => {
		display = currentDisplay;
	});


</script>


<Header /> 

<main class="grid place-items-center">
  {#if display == 0}
  <title> Voting </title>
    <Voting bind:results={$results} />
  {:else if display == 1}
  <title> Results </title>
    <Results />
  {:else if display == 2}
  <title> Completed Ballots </title>
    <CompletedBallots />
  {:else}
  {#if $username === ""}
  <title> Login </title>
    <Login />
  {:else}
  <title> Voting </title>
    <Voting bind:results={$results} />
  {/if}
  {/if}
</main>
