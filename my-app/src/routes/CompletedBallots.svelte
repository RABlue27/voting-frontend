<script>



let data = {
  "Year": 2023,
  "Weeks": [
    {
      "WeekNumber": 1,
      "Players": [
        {
          "Name": "Mike Trout",
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
      "WeekNumber": 2,
      "Players": [
        {
          "Name": "Fernando Tatis Jr.",
          "Comment": "His energy and flair bring excitement to the game."
        },
        {
          "Name": "Shohei Ohtani",
          "Comment": "A two-way star, excelling as both a pitcher and hitter."
        },
        {
          "Name": "Freddie Freeman",
          "Comment": "Consistent hitter and leader for the Atlanta Braves."
        },
        {
          "Name": "Gerrit Cole",
          "Comment": "Crafty pitcher with excellent command and repertoire."
        }
      ]
    },
    {
      "WeekNumber": 3,
      "Players": [
        {
          "Name": "Vladimir Guerrero Jr.",
          "Comment": "Continues to impress with his hitting prowess."
        },
        {
          "Name": "Xander Bogaerts",
          "Comment": "An essential player for the Boston Red Sox."
        },
        {
          "Name": "Max Scherzer",
          "Comment": "Unyielding intensity and masterful pitching."
        },
        {
          "Name": "Bryce Harper",
          "Comment": "A fierce competitor with an undeniable passion for the game."
        }
      ]
    }
    
  ]
}

</script>

<table class="w-full h-full">
  <thead>
    <tr class="w-full text-left">
      <th class="p-2">Week</th>
      <th class="p-2">Name</th>
      <th class="p-2">Comment</th>
    </tr>
  </thead>
  <tbody>
    {#each data.Weeks as week}
    <tr class="bg-gray-900">
      <td colspan="3" class="p-2">
        <h2 class="text-white font-semibold">Week {week.WeekNumber}</h2>
      </td>
    </tr>
    {#each week.Players as player, index}
    <tr class="{index % 2 === 0 ? 'bg-gray-200' : 'bg-gray-300'}">
      <td class="p-2"></td>
      <td class="p-2">{player.Name}</td>
      <td class="p-2">{player.Comment}</td>
    </tr>
    {/each}
    {/each}
  </tbody>
</table>
