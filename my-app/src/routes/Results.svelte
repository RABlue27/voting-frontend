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
          "Votes": 5,
          "Comments": [
            {
              "Username": "Commenter 1",
              "Comment": "Comment 1"
            },
            {
              "Username": "Commenter 2",
              "Comment": "Comment 2"
            }
          ]
        },
        {
          "Name": "Pitcher Name 2",
          "Votes": 0,
          "Comments": [
            {
              "Username": "Commenter 3",
              "Comment": "Comment 3"
            },
            {
              "Username": "Commenter 4",
              "Comment": "Comment 4"
            }
          ]
        }
      ],
      "Hitters": [
        {
          "Name": "Hitter Name 1",
          "Votes": 0,
          "Comments": [
            {
              "Username": "Commenter 5",
              "Comment": "Comment 5"
            },
            {
              "Username": "Commenter 6",
              "Comment": "Comment 6"
            }
          ]
        },
        {
          "Name": "Hitter Name 2",
          "Votes": 0,
          "Comments": [
            {
              "Username": "Commenter 7",
              "Comment": "Comment 7"
            },
            {
              "Username": "Commenter 8",
              "Comment": "Comment 8"
            }
          ]
        }
      ]
    },
    "NL": {
      "Pitchers": [
        {
          "Name": "Pitcher Name 1",
          "Votes": 0,
          "Comments": [
            {
              "Username": "Commenter 9",
              "Comment": "Comment 9"
            },
            {
              "Username": "Commenter 10",
              "Comment": "Comment 10"
            }
          ]
        },
        {
          "Name": "Pitcher Name 2",
          "Votes": 0,
          "Comments": [
            {
              "Username": "Commenter 11",
              "Comment": "Comment 11"
            },
            {
              "Username": "Commenter 12",
              "Comment": "Comment 12"
            }
          ]
        }
      ],
      "Hitters": [
        {
          "Name": "Hitter Name 1",
          "Votes": 0,
          "Comments": [
            {
              "Username": "Commenter 13",
              "Comment": "Comment 13"
            },
            {
              "Username": "Commenter 14",
              "Comment": "Comment 14"
            }
          ]
        },
        {
          "Name": "Hitter Name 2",
          "Votes": 0,
          "Comments": [
            {
              "Username": "Commenter 15",
              "Comment": "Comment 15"
            },
            {
              "Username": "Commenter 16",
              "Comment": "Comment 16"
            }
          ]
        }
      ]
    }
  }
}



</script>

{#each Object.entries(data.Results) as [league, category]}
  <h2 class="text-2xl font-bold mt-4 mb-2">{league}</h2>
  {#each Object.entries(category) as [categoryName, players]}
    <h3 class="text-xl font-semibold mt-2 mb-1">{categoryName}</h3>
    <table class="w-full border-collapse border rounded-lg overflow-hidden">
      <thead>
        <tr class="bg-gray-900 text-white">
          <th class="px-4 py-2 font-semibold text-left">Player</th>
          <th class="px-4 py-2 font-semibold text-left">Votes</th>
        </tr>
      </thead>
      <tbody>
        {#each players as player, index}
        <tr class="{index % 2 === 0 ? 'bg-gray-200' : 'bg-gray-300'}">
          <td class="px-4 py-2 border w-8/12">{player.Name}</td>
          <td class="px-4 py-2 border w-8/12">
            <button class="bg-teal-700 hover:bg-teal-800 active:bg-teal-900 text-white px-2 py-1 rounded w-full h-full {player.showDetails ? 'bg-teal-900' : ''}" on:click={() => (player.showDetails = !player.showDetails)} style="width: 100%;">
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
