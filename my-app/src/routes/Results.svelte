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
          "Name": "Shohei Ohtani",
          "Votes": 5,
          "Comments": [
            {
              "Username": "user1",
              "Comment": "Impressive performance as a two-way player."
            },
            {
              "Username": "user2",
              "Comment": "Ohtani's versatility is unmatched."
            }
          ]
        },
        {
          "Name": "Gerrit Cole",
          "Votes": 3,
          "Comments": [
            {
              "Username": "user3",
              "Comment": "Consistently dominant on the mound."
            },
            {
              "Username": "user4",
              "Comment": "Great control and pitching repertoire."
            }
          ]
        }
      ],
      "Hitters": [
        {
          "Name": "Vladimir Guerrero Jr.",
          "Votes": 2,
          "Comments": [
            {
              "Username": "user5",
              "Comment": "An incredible breakout season for Vlad Jr."
            },
            {
              "Username": "user6",
              "Comment": "Consistent hitting and power."
            }
          ]
        },
        {
          "Name": "Xander Bogaerts",
          "Votes": -1,
          "Comments": [
            {
              "Username": "user7",
              "Comment": "Underrated player with great offensive skills."
            },
            {
              "Username": "user8",
              "Comment": "Smooth fielding and clutch hitting."
            }
          ]
        }
      ]
    },
    "NL": {
      "Pitchers": [
        {
          "Name": "Jacob deGrom",
          "Votes": 6,
          "Comments": [
            {
              "Username": "user9",
              "Comment": "DeGrom is simply the best pitcher in the game."
            },
            {
              "Username": "user10",
              "Comment": "Unbelievable stuff and command."
            }
          ]
        },
        {
          "Name": "Max Scherzer",
          "Votes": 0,
          "Comments": [
            {
              "Username": "user11",
              "Comment": "Scherzer's intensity and competitiveness are unmatched."
            },
            {
              "Username": "user12",
              "Comment": "A true ace with a dominant presence on the mound."
            }
          ]
        }
      ],
      "Hitters": [
        {
          "Name": "Fernando Tatis Jr.",
          "Votes": 5,
          "Comments": [
            {
              "Username": "user13",
              "Comment": "Exciting player with great energy and skill."
            },
            {
              "Username": "user14",
              "Comment": "A true game-changer with his abilities."
            }
          ]
        },
        {
          "Name": "Bryce Harper",
          "Votes": 1,
          "Comments": [
            {
              "Username": "user15",
              "Comment": "Harper's power and charisma make him a fan favorite."
            },
            {
              "Username": "user16",
              "Comment": "Always a threat at the plate and a solid defender."
            }
          ]
        }
      ]
    }
  }
}


</script>

<button on:click={() => { ballots() }}>Back to Ballots</button>

{#each Object.entries(data.Results) as [league, category]}
  <h2>{league}</h2>
  {#each Object.entries(category) as [categoryName, players]}
    <h3>{categoryName}</h3>
    <table>
      <thead>
        <tr>
          <th>Player</th>
          <th>Votes</th>
        </tr>
      </thead>
      <tbody>
        {#each players as player}
          <tr>
            <td>{player.Name}</td>
            <td>
              <button on:click={() => (player.showDetails = !player.showDetails)}>
                {player.Votes}
              </button>
            </td>
          </tr>
          {#if player.showDetails}
            <tr>
              <td colspan="2">
                <ul>
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

<style>

table {
  width: 100%;
  border-collapse: collapse;
}

/* Table Head */
thead {
  background-color: #333;
  color: #fff;
}

thead th {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #555;
}

/* Table Body */
tbody {
  background-color: #222;
}

tbody td {
  padding: 10px;
  border-bottom: 1px solid #555;
  color: #fff; 
}

/* Alternate row color */
tbody tr:nth-child(even) {
  background-color: #333;
}

/* Player */
tbody td:first-child {
  width: 30%; /* Adjust the width as needed */
  max-width: 200px; 
  overflow: hidden;
  text-overflow: ellipsis; 
  white-space: nowrap;
}

/* Player details */
tbody td[colspan="2"] ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

tbody td[colspan="2"] li {
  padding: 5px;
}

tbody td[colspan="2"] li strong {
  font-weight: bold;
  color: #fff;
}

/* Button */
button {
  padding: 5px 10px;
  background-color: #555;
  border: none;
  color: #fff;
  cursor: pointer;
  display: inline-block; 
  vertical-align: middle; 
}

button:hover {
  background-color: #777;
}

</style>