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
    }
  ]
}

</script>


<h1>MLB Players</h1>

<table>
    <thead>
      <tr>
        <th>Week</th>
        <th>Name</th>
        <th>Comment</th>
      </tr>
    </thead>
    <tbody>
      {#each data.Weeks as week}
      <tr>
        <td colspan="3">
          <h2>Week {week.WeekNumber}</h2>
        </td>
      </tr>
      {#each week.Players as player}
      <tr>
        <td></td>
        <td>{player.Name}</td>
        <td>{player.Comment}</td>
      </tr>
      {/each}
      {/each}
    </tbody>
  </table>

<style>

table {
  width: 100%;
  border-collapse: collapse;
}

h1 {
  color: white;
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
  color: #fff; /* Updated text color */
}

/* Alternate row color */
tbody tr:nth-child(even) {
  background-color: #333;
}



</style>