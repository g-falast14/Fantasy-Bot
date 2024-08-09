from yahoo_fantasy_api import Team
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

# connect to yahoo api
sc = OAuth2(None, None, from_file="oauth2.json")

# get game objet
gm = yfa.Game(sc, 'nhl')

leagues = gm.league_ids()

# print(leagues)

# get the league object
# league = gm.to_league(leagues[0])
league = gm.to_league('453.l.438')

# get all teams in league (stored in dictionary with team key as keys and team info as values)
# create list to store teams
teamsList = []
for teamKey in league.teams():
    team = Team(sc, teamKey)
    teamsList.append(team)

randomTeam = teamsList[0]
print(randomTeam.details())




# for teamKey in teams:
#     teamList.push(teamKey.to_team())

