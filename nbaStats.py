import requests
from bs4 import BeautifulSoup

# Getting the data from ESPN
data = requests.get('https://www.espn.com/nba/stats/player/_/table/offensive/sort/avgPoints/dir/desc')
