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


<main class="grid place-items-center sm:w-full lg:w-2/3 xl:w-3/5 2xl:w-11/12">
<Header /> 

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
