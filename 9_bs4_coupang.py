import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

items = soup.find_all('li', attrs={'class': re.compile('^search-product')})
for item in items:

    # 사전예약 제품은 제외
    pre_order = item.find('span', attrs={'class': 'pre-order-badge-text'})
    if pre_order:
        print('   > 사전예약 제품은 제외합니다.')
        continue

    # 1. 제품명
    name = item.find('div', attrs={'class': 'name'}).get_text()
    # 1-1. Apple 제품은 제외
    if 'Apple' in name or '맥북' in name:
        print('   > 애플 제품은 제외합니다.')
        continue

    # 2. 가격
    price = item.find('strong', attrs={'class': 'price-value'}).get_text()

    # 3. 평점 & 평점 수
    rating = item.find('em', attrs={'class': 'rating'})
    if rating:
        rating = rating.get_text()
    else:
        print('   > 평점 없는 제품은 제외합니다.')
        continue

    rating_cnt = item.find(
        'span', attrs={'class': 'rating-total-count'})  # 평점 수
    if rating_cnt:
        rating_cnt = rating_cnt.get_text()
        rating_cnt = rating_cnt[1:-1]
    else:
        print('   > 평점 수 없는 제품은 제외합니다.')
        continue
    # 3-1. 평점 & 평점 수 필터링(리뷰 1000개 이상, 평점 4.5 이상)
    if float(rating) >= 4.5 and int(rating_cnt) >= 1000:
        print(name, price, rating, rating_cnt)
