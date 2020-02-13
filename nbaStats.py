import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# Getting the data from ESPN
data = requests.get('https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc')

# Load the data into BeautifulSoup
soup = BeautifulSoup(data.text, 'html.parser')

statTable = soup.find('table')
tbody = statTable.find('tbody')

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


# Create and write nbaStats.csv file.
d = [rankList, playerList, teamList]
export_data = zip_longest(*d, fillvalue= '')
with open('nbaStats.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(('Rank', 'Player', 'Team'))
    writer.writerows(export_data)
