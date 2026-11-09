import requests
from bs4 import BeautifulSoup

url = "https://cactslearn.github.io/sitemap.xml"
response = requests.get(url, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
# print('Title', soup.find('title').get_text(strip = True))
print(soup.prettify())

# for link in soup.find_all('a', href= True):
#     print(link.get_text(strip=True), link['href'])