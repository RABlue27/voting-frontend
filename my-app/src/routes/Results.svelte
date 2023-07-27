<script> 

import {voted, currentDisplay} from "./stores.js";
function ballots() {
    voted.set(!$voted);
    currentDisplay.set(0);
  }


let data = {
  "Results": {
    "AL": {
      "Pitchers": [
        {
          "Name": "Pitcher Name 1",
          "Votes": 7,
          "Comments": [{"Username": "Commenter 1", "Comment": "Comment 1"}, {"Username": "Commenter 2", "Comment": "Comment 2"}, {"Username": "Commenter 3", "Comment": "Comment 3"}]
        },
        {
          "Name": "Pitcher Name 2",
          "Votes": 3,
          "Comments": [{"Username": "Commenter 4", "Comment": "Comment 4"}]
        }
      ],
      "Hitters": [
        {
          "Name": "Hitter Name 1",
          "Votes": 1,
          "Comments": [{"Username": "Commenter 5", "Comment": "Comment 5"}]
        },
        {
          "Name": "Hitter Name 2",
          "Votes": 2,
          "Comments": [{"Username": "Commenter 6", "Comment": "Comment 6"}, {"Username": "Commenter 7", "Comment": "Comment 7"}]
        }
      ]
    },
    "NL": {
      "Pitchers": [
        {
          "Name": "Pitcher Name 1",
          "Votes": 6,
          "Comments": [{"Username": "Commenter 8", "Comment": "Comment 8"}]
        },
        {
          "Name": "Pitcher Name 2",
          "Votes": 4,
          "Comments": [{"Username": "Commenter 9", "Comment": "Comment 9"}, {"Username": "Commenter 10", "Comment": "Comment 10"}, {"Username": "Commenter 11", "Comment": "Comment 11"}]
        }
      ],
      "Hitters": [
        {
          "Name": "Hitter Name 1",
          "Votes": 5,
          "Comments": [{"Username": "Commenter 12", "Comment": "Comment 12"}, {"Username": "Commenter 13", "Comment": "Comment 13"}]
        },
        {
          "Name": "Hitter Name 2",
          "Votes": 8,
          "Comments": [{"Username": "Commenter 14", "Comment": "Comment 14"}]
        }
      ]
    }
  }
}



</script>



<div class="w-8/12 mx-auto">
  {#each Object.entries(data.Results) as [league, category]}
    <h2 class="text-2xl font-bold mt-4 mb-2 underline">{league}</h2>
    {#each Object.entries(category) as [categoryName, players]}
      <h3 class="text-xl font-semibold mt-2 mb-1">{categoryName}</h3>
      <table class="w-full border-collapse border overflow-hidden bg-black  rounded-lg ">
        <thead>
          <tr class="bg-teal-400 text-white">
            <th class="px-4 py-2 font-medium text-left">Player</th>
            <th class="px-4 py-2 font-medium text-left">Votes</th>
          </tr>
        </thead>
        <tbody>
          {#each players as player, index}
          <tr class="{index % 2 === 0 ? 'bg-gray-200' : 'bg-gray-300'}">
            <td class="px-4 py-2 border w-8/12">{player.Name}</td>
            <td class="px-4 py-2 border w-4/12">
              <button class="bg-teal-400 hover:bg-teal-500 active:bg-teal-600 text-white px-2 py-1 rounded w-full {player.showDetails ? 'bg-teal-600' : ''}" on:click={() => (player.showDetails = !player.showDetails)}>
                {player.Votes}
              </button>
            </td>
          </tr>
          {#if player.showDetails}
            <tr class="{index % 2 === 0 ? 'bg-gray-200' : 'bg-gray-300'}">
              <td class="px-4 py-2 border" colspan="2">
                <ul class="list-disc list-inside">
                  {#each player.Comments as comment}
                    <li>
                      <strong>{comment.Username}</strong>: {comment.Comment}
                    </li>
                  {/each}
                </ul>
              </td>
            </tr>
          {/if}
          {/each}
        </tbody>
      </table>
    {/each}
  {/each}
</div>
