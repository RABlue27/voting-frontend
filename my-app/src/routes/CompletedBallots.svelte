<script>



  let data = {
"Year": 2023,
"Weeks": [
  {
    "WeekNumber": "1/2",
    "Players": [
      {
        "Name": "Mike Trout",
        "Div": "AL",
        "Pos": "Hitter",
        "Comment": "He's an incredible all-around player."
      },
      {
        "Name": "Mookie Betts",
        "Comment": "Known for his exceptional fielding skills."
      },
      {
        "Name": "Ronald Acuña Jr.",
        "Comment": "A dynamic player with speed and power."
      },
      {
        "Name": "Jacob deGrom",
        "Comment": "Dominant pitcher with an electric fastball."
      }
    ]
  },
  {
    "WeekNumber": "3",
    "Players": [
      {
        "Name": "Vladimir Guerrero Jr.",
        "Div": "AL",
        "Pos": "Hitter",
        "Comment": "Continues to live up to his family's legacy."
      },
      {
        "Name": "Fernando Valenzuela",
        "Comment": "Mexican lefty known for his screwball pitch."
      },
      {
        "Name": "Bryce Harper",
        "Comment": "Powerful hitter and charismatic presence."
      },
      {
        "Name": "Gleyber Torres",
        "Comment": "Young talent with a promising future."
      }
    ]
  },
  {
    "WeekNumber": "4",
    "Players": [
      {
        "Name": "Shohei Ohtani",
        "Div": "AL",
        "Pos": "Two-Way Star",
        "Comment": "An extraordinary talent on the mound and at the plate."
      },
      {
        "Name": "Max Scherzer",
        "Comment": "Crafty veteran pitcher with multiple Cy Young awards."
      },
      {
        "Name": "Francisco Lindor",
        "Comment": "Dynamic shortstop with a mix of power and defense."
      },
      {
        "Name": "Anthony Rendon",
        "Comment": "Solid third baseman with great hitting skills."
      }
    ]
  },
  {
    "WeekNumber": "5",
    "Players": [
      {
        "Name": "Freddie Freeman",
        "Div": "NL",
        "Pos": "Hitter",
        "Comment": "Consistent hitter and leader for the Atlanta Braves."
      },
      {
        "Name": "Clayton Kershaw",
        "Comment": "Crafty left-handed pitcher and Dodgers icon."
      },
      {
        "Name": "José Abreu",
        "Comment": "Powerful first baseman with a great batting eye."
      },
      {
        "Name": "Xander Bogaerts",
        "Comment": "Smooth-fielding shortstop with offensive prowess."
      }
    ]
  },
  {
    "WeekNumber": "May",
    "Players": [
      {
        "Name": "Aaron Judge",
        "Comment": "Massive power hitter and fan favorite."
      },
      {
        "Name": "Walker Buehler",
        "Comment": "Young pitcher with a fiery fastball and composure."
      },
      {
        "Name": "Yordan Álvarez",
        "Comment": "Slugger with incredible raw power."
      },
      {
        "Name": "Trevor Story",
        "Comment": "Shortstop known for his defensive skills and homers."
      }
    ]
  }
]
}
let numWeeksToShow = 1;
function addWeek() {
  // Increase the number of weeks to show if it's less than the total number of weeks
  if (numWeeksToShow < data.Weeks.length) {
    numWeeksToShow += 1;
  }
}

function removeWeek() {
  // Decrease the number of weeks to show if it's greater than 1
  if (numWeeksToShow >= 1) {
    numWeeksToShow -= 1;
  }
}
  </script>
  
<div class="border-black rounded-sm border-2 w-7/12 mt-4">
<table class="w-full h-full">
  <thead>
    <tr class="w-full text-left bg-teal-400 text-white border-black border-b-2">
      <th class="p-2">Week</th>
      <th class="p-2">Name</th>
      <th class="p-2">Comment</th>
    </tr>
  </thead>
  <tbody>
    {#each data.Weeks.slice(0, numWeeksToShow) as week}
      <tr class="border-r-0 border-l-0">
        <td colspan="3" class="p-2 font-semibold text-black">
          { !isNaN(week.WeekNumber[0]) ? "Week " + week.WeekNumber : week.WeekNumber}
        </td>
      </tr>
      {#each week.Players as player, index}
        <tr class="{index % 2 === 0 ? 'bg-gray-100' : 'bg-gray-200'}">
          <td class="p-2"></td>
          <td class="p-2">{player.Name}</td>
          <td class="p-2">{player.Comment}</td>
        </tr>
      {/each}
    {/each}
  </tbody>
</table>
</div>

<div class="flex space-x-3">
<button on:click={addWeek} class="mt-4 bg-blue-500 text-white font-semibold px-4 py-2 rounded hover:bg-blue-600 w-22">
Add week
</button>
<button on:click={removeWeek} class="mt-4 bg-blue-500 text-white font-semibold px-4 py-2 rounded hover:bg-blue-600 w-22">
  Remove Week
</button>
</div> 