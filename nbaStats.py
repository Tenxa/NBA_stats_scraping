import requests
from bs4 import BeautifulSoup
import csv

# Getting the data from ESPN
data = requests.get('https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc')

# Load the data into BeautifulSoup
soup = BeautifulSoup(data.text, 'html.parser')

statTable = soup.find('table')
tbody = statTable.find('tbody')

rows = []
# Looping through all the rows and getting rank, player and team data.
for tr in tbody.find_all('tr'):
    rank = tr.find_all('td')[0].text
    player = tr.find_all('td')[1].find_all('a')[0].text
    team = tr.find_all('td')[1].find_all('span')[0].text
    rows.append(rank+"," +player+"," +team)


with open('nbaStats.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in rows:
        writer.writerow([row])