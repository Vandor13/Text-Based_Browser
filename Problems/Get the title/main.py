import requests

from bs4 import BeautifulSoup

url = input()

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

heading = soup.find("h1")
# print(hyperlinks)
soup2 = BeautifulSoup(str(heading), 'html.parser')
heading = soup2.get_text()
print(heading)