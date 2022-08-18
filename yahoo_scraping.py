from bs4 import BeautifulSoup
import requests

rainy_percent = [] #出力用の変数

url = 'https://weather.yahoo.co.jp/weather/8/4010/8202.html'
res = requests.get(url) #urlの情報を取得
 #Webサイトを解析
soup = BeautifulSoup(res.text, "html.parser")
elems = soup.find_all("td")


 #今日の天気の降水量を抽出し、今日雨が降るか確認
today = 0

for i in range(41, 49):
    if (int(elems[i].contents[1].contents[0]) > 0):
        today = 100

rainy_percent.append(today)

 #週間天気の降水確率(%)を抽出
for i in range(132, 138):
    """
    print(elems[i].contents[1].contents[0]) #数字のみを抽出
    print('\n')
    """
    rainy_percent.append(int(elems[i].contents[1].contents[0]))

print(rainy_percent)
