from bs4 import BeautifulSoup
import requests

rainy_percent = []

url = 'https://weather.yahoo.co.jp/weather/8/4010/8202.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
elems = soup.find_all("td")


today = 0
"""
for i in range(41, 49):
	if (int(elems[i].contents[1].contents[0]) > 0):
		today = 100
"""
rainy_percent.append(today)

for i in range(132, 138):
	rainy_percent.append(int(elems[i].contents[1].contents[0]))
	
print(rainy_percent)
