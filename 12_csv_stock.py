import csv
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/sise_market_sum.nhn?&page='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
filename = '시가총액1-200.csv'
f = open(filename, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)

# Header
title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE'.split('\t')
writer.writerow(title)

# Table Content
for page in range(1, 5):
    res = requests.get(url+str(page), headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    data_rows = soup.find('table', attrs={'class': 'type_2'}).find(
        'tbody').find_all('tr')
    for row in data_rows:
        columns = row.find_all('td')
        if len(columns) <= 1:
            continue
        data = [x.get_text().strip() for x in columns]
        # print(data)
        writer.writerow(data)
