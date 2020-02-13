import requests
from bs4 import BeautifulSoup

# Getting the data from ESPN
data = requests.get('https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc')

# Load the data into BeautifulSoup
soup = BeautifulSoup(data.text, 'html.parser')

statTable = soup.find('table')
tbody = statTable.find('tbody')

for tr in tbody.find_all('tr'):
    rank = tr.find_all('td')[0].text
    player = tr.find_all('td')[1].find_all('a')[0].text
    print(rank, player)