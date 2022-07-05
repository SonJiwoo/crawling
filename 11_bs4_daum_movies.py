import requests
import re
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

for year in range(2017, 2022):
    url = 'https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(
        year)
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    images = soup.find_all('img', attrs={'class': 'thumb_img'})
    for idx, image in enumerate(images):
        image_url = image['src']
        image_res = requests.get(image_url, headers=headers)
        image_res.raise_for_status()

        with open('{}_movie{}.jpg'.format(year, idx+1), 'wb') as f:
            f.write(image_res.content)

        if idx >= 4:  # 상위 5위까지만 다운로드
            break
