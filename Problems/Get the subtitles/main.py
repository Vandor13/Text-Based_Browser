import requests

from bs4 import BeautifulSoup

subtitle_index = int(input())
url = input()

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find_all("h2")[subtitle_index]
soup2 = BeautifulSoup(str(title), 'html.parser')
title = soup2.get_text()
print(title)
