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
        "Name": "Justin Verlander",
        "Votes": 92,
        "Comments": [
          {"Username": "BaseballFan123", "Comment": "Verlander is a true ace."},
          {"Username": "PitchingAce", "Comment": "He's been carrying the team on his back."},
          {"Username": "MLBExpert99", "Comment": "Verlander's experience is evident in his performance."}
        ]
      },
      {
        "Name": "Gerrit Cole",
        "Votes": 87,
        "Comments": [
          {"Username": "AstrosNation", "Comment": "Cole's strikeouts are a sight to see."},
          {"Username": "FastballFanatic", "Comment": "Cole's fastball is electric."},
          {"Username": "CurveballKing", "Comment": "His curveball is a work of art."}
        ]
      }
    ],
    "Hitters": [
      {
        "Name": "Mike Trout",
        "Votes": 95,
        "Comments": [
          {"Username": "AngelsFan22", "Comment": "Trout is the best player in the game."},
          {"Username": "HomeRunHero", "Comment": "Another day, another Trout home run."},
          {"Username": "MVPChants", "Comment": "Trout's consistency is astonishing."}
        ]
      },
      {
        "Name": "José Altuve",
        "Votes": 78,
        "Comments": [
          {"Username": "AstrosLover", "Comment": "Altuve's small stature doesn't stop him."},
          {"Username": "BatFlipMaster", "Comment": "Altuve's bat flips are legendary."}
        ]
      }
    ]
  },
  "NL": {
    "Pitchers": [
      {
        "Name": "Jacob deGrom",
        "Votes": 93,
        "Comments": [
          {"Username": "MetsMania", "Comment": "deGrom is the heart and soul of the Mets."},
          {"Username": "StrikeoutMachine", "Comment": "His strikeouts are a work of art."},
          {"Username": "AmazingSlider", "Comment": "deGrom's slider is unhittable."}
        ]
      },
      {
        "Name": "Max Scherzer",
        "Votes": 88,
        "Comments": [
          {"Username": "NatsNation", "Comment": "Scherzer's intensity is unmatched."},
          {"Username": "MadMaxFanatic", "Comment": "Max is a true warrior on the mound."},
          {"Username": "ScherzerSizzle", "Comment": "Scherzer's passion for the game is inspiring."}
        ]
      }
    ],
    "Hitters": [
      {
        "Name": "Freddie Freeman",
        "Votes": 85,
        "Comments": [
          {"Username": "BravesCountry", "Comment": "Freddie Freeman is a Braves legend."},
          {"Username": "ClutchHitsOnly", "Comment": "Freddie delivers when it matters most."},
          {"Username": "NL_MVP", "Comment": "He's a strong contender for the NL MVP."}
        ]
      },
      {
        "Name": "Mookie Betts",
        "Votes": 89,
        "Comments": [
          {"Username": "DodgersDynasty", "Comment": "Mookie Betts is a game-changer."},
          {"Username": "BettsBeliever", "Comment": "Betts' all-around skills are unmatched."},
          {"Username": "SpeedDemon", "Comment": "Mookie's speed adds another dimension to his game."}
        ]
      }
    ]
  }
}
}

  
  let month=  {
"Results": {
  "AL": {
    "Pitchers": [
      {
        "Name": "James Paxton",
        "Votes": 12,
        "Comments": [
          {"Username": "PitchingFan1", "Comment": "Paxton's curveball is a thing of beauty."}
        ]
      },
      {
        "Name": "Zack Greinke",
        "Votes": 8,
        "Comments": [
          {"Username": "AstrosNation", "Comment": "Greinke's changeup is masterful."},
          {"Username": "GreinkeFanatic", "Comment": "I'm always amazed by his control on the mound."}
        ]
      }
    ],
    "Hitters": [
      {
        "Name": "Anthony Rendon",
        "Votes": 7,
        "Comments": [
          {"Username": "AngelsFan22", "Comment": "Rendon's swing is a work of art."}
        ]
      },
      {
        "Name": "Gleyber Torres",
        "Votes": 4,
        "Comments": [
          {"Username": "YankeesNation", "Comment": "Torres has a bright future ahead."},
          {"Username": "DoublePlayMaster", "Comment": "His defensive plays are impressive."}
        ]
      }
    ]
  },
  "NL": {
    "Pitchers": [
      {
        "Name": "Walker Buehler",
        "Votes": 10,
        "Comments": [
          {"Username": "DodgersDynasty", "Comment": "Buehler's fastball has serious heat."},
          {"Username": "PitchingAce", "Comment": "His composure on the mound is remarkable."}
        ]
      },
      {
        "Name": "Yu Darvish",
        "Votes": 6,
        "Comments": [
          {"Username": "CubsNation", "Comment": "Darvish's pitch repertoire keeps hitters off balance."}
        ]
      }
    ],
    "Hitters": [
      {
        "Name": "Ronald Acuña Jr.",
        "Votes": 9,
        "Comments": [
          {"Username": "BravesCountry", "Comment": "Acuña Jr.'s speed adds excitement to the game."},
          {"Username": "PowerHitter", "Comment": "His home runs are a thing of beauty."}
        ]
      },
      {
        "Name": "Fernando Tatis Jr.",
        "Votes": 11,
        "Comments": [
          {"Username": "PadresFanatic", "Comment": "Tatis Jr. is a spark plug for the Padres."},
          {"Username": "DynamicPlayer", "Comment": "His energy on the field is infectious."},
          {"Username": "SwagSwing", "Comment": "Tatis Jr.'s unique swing is captivating."}
        ]
      }
    ]
  }
}
}


  
  let isMonthly = month.length;
  
  </script>
  
  <div class="w-8/12 mx-auto mb-12">
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
  
  {#if isMonthly}
  <p class="text-5xl"> Monthly Results </p>
  
  <div class="w-8/12 mx-auto mb-12">
    {#each Object.entries(month.Results) as [league, category]}
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
  
  {/if}

  <p> Toggle Monthly Status </p>
  <input type="checkbox" class="form-checkbox h-5 w-5 text-indigo-600 mb-12" bind:checked={isMonthly}>
