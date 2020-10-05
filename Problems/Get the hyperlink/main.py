import requests

from bs4 import BeautifulSoup

subtitle_index = int(input())
url = input()

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

hyperlinks = soup.find_all("a")
# print(hyperlinks)
# print(hyperlinks)

print(hyperlinks[subtitle_index-1]['href'])
