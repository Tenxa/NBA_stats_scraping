import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# Getting the data from ESPN
data = requests.get('https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc')

# Load the data into BeautifulSoup
soup = BeautifulSoup(data.text, 'html.parser')

rankNameTable = soup.find('table')
tbody = rankNameTable.find('tbody')

# made 3 lists as ESPN includes team and player name in the NAME column.
rankList = []
playerList = []
teamList = []

# Looping through all the rows and getting rank, player and team data.
for tr in tbody.find_all('tr'):
    rank = tr.find_all('td')[0].text
    rankList.append(rank)
    player = tr.find_all('td')[1].find_all('a')[0].text
    playerList.append(player)
    team = tr.find_all('td')[1].find_all('span')[0].text
    teamList.append(team)

# Going to the second table that contains the game stats
statsTable = soup.find('table', {'class': 'Table Table--align-right'})
statsTbody = statsTable.find('tbody')

positions = []
gamesPlayed = []
ptsAVG = []
FGAttempts = []
FGpercentages = []
threePointAttempts = []
threePointPercentages = []

for tr in statsTbody.find_all('tr'):
    position = tr.find_all('td')[0].text
    positions.append(position)
    gp = tr.find_all('td')[1].text
    gamesPlayed.append(gp)
    pts = tr.find_all('td')[3].text
    ptsAVG.append(pts)
    fga = tr.find_all('td')[5].text
    FGAttempts.append(fga)
    fgp = tr.find_all('td')[6].text
    FGpercentages.append(fgp)
    threePA = tr.find_all('td')[8].text
    threePointAttempts.append(threePA)
    threePP = tr.find_all('td')[9].text
    threePointPercentages.append(threePP)

# Create and write nbaStats.csv file.
d = [rankList, playerList, teamList, positions, gamesPlayed, ptsAVG, FGAttempts,
     FGpercentages, threePointAttempts, threePointPercentages]
export_data = zip_longest(*d, fillvalue= '')
with open('nbaStats.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(('Rank', 'Player', 'Team', 'POS', 'GP',
                     'PPG', 'FGA', 'FG%',
                     '3PTA', '3PT%'))
    writer.writerows(export_data)
