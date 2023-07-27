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
      "WeekNumber": "June",
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
    }
  ]
}

</script>


<div class=" border-black rounded-sm border-2 w-7/12 mt-4">
  <table class="w-full h-full">
    <thead>
      <tr class="w-full text-left bg-teal-400 text-white border-black border-b-2">
        <th class="p-2">Week</th>
        <th class="p-2">Name</th>
        <th class="p-2">Comment</th>
      </tr>
    </thead>
    <tbody>
      {#each data.Weeks as week}
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
