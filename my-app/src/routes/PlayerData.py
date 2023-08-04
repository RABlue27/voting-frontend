import json
from pybaseball import statcast
import statsapi


def get_team_abbreviation(team_id):
    team_ids = {
        109: 'ARI',
        144: 'ATL',
        110: 'BAL',
        111: 'BOS',
        145: 'CWS',
        112: 'CHC',
        113: 'CIN',
        114: 'CLE',
        115: 'COL',
        116: 'DET',
        117: 'HOU',
        118: 'KC',
        108: 'LAA',
        119: 'LAD',
        146: 'MIA',
        158: 'MIL',
        142: 'MIN',
        147: 'NYY',
        121: 'NYM',
        133: 'OAK',
        143: 'PHI',
        134: 'PIT',
        135: 'SD',
        137: 'SF',
        136: 'SEA',
        138: 'STL',
        139: 'TB',
        140: 'TEX',
        141: 'TOR',
        120: 'WSH'
    }
    
    return team_ids.get(team_id)


statcast_data = statcast(start_dt="2023-01-01", end_dt="2023-08-04")


player_names = statcast_data['player_name'].unique()


formatted_player_names = [" ".join(name.split()[::-1]).replace(',', '').strip() for name in player_names]


sorted_formatted_player_names = sorted(formatted_player_names)


results = []


processed_players = set() 

for name in sorted_formatted_player_names:
    last_name, first_name = name.split(' ', 1)
    try:
        for player in statsapi.lookup_player(last_name):
            player_name = player['fullName']
            
            # Skip player if already processed
            if player_name in processed_players:
                continue
            
            # Mark player as processed
            processed_players.add(player_name)
            
            player_data = {
                'Full name': player_name,
                'Position': player['primaryPosition']['abbreviation'],
                'Team': get_team_abbreviation(player['currentTeam']['id'])
            }
            results.append(player_data)
    except Exception as e:
        print(f"An error occurred for player {name}: {e}")


json_results = json.dumps(results, indent=2)


# Write the encoded player names to a JavaScript file with proper formatting
js_code = f"export const playersList = {json_results};\n"
js_filename = 'my-app/src/routes/playerList.js'
with open(js_filename, 'w', encoding='utf-8') as js_file:
    js_file.write(js_code)

print("done!")
