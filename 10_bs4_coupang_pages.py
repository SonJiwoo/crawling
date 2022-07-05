import requests
import re
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
for i in range(1, 11):
    url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor='.format(
        i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    items = soup.find_all('li', attrs={'class': re.compile('^search-product')})
    for item in items:

        # 사전예약 제품은 제외
        pre_order = item.find('span', attrs={'class': 'pre-order-badge-text'})
        if pre_order:
            # print('   > 사전예약 제품은 제외합니다.')
            continue

        # 1. 제품명
        name = item.find('div', attrs={'class': 'name'}).get_text()
        # 1-1. Apple 제품은 제외
        if 'Apple' in name or '맥북' in name:
            # print('   > 애플 제품은 제외합니다.')
            continue

        # 2. 가격
        price = item.find('strong', attrs={'class': 'price-value'})
        if price:
            price = price.get_text()
        else:
            # print('   > 가격이 없는 제품은 제외합니다.')
            continue

        # 3. 평점 & 평점 수
        rating = item.find('em', attrs={'class': 'rating'})
        if rating:
            rating = rating.get_text()
        else:
            # print('   > 평점 없는 제품은 제외합니다.')
            continue

        rating_cnt = item.find(
            'span', attrs={'class': 'rating-total-count'})  # 평점 수
        if rating_cnt:
            rating_cnt = rating_cnt.get_text()[1:-1]
        else:
            # print('   > 평점 수 없는 제품은 제외합니다.')
            continue
        # 3-1. 평점 & 평점 수 필터링(리뷰 1000개 이상, 평점 4.5 이상)

        # 4. 링크
        link = item.find('a', attrs={'class': 'search-product-link'})['href']

        if float(rating) >= 4.5 and int(rating_cnt) >= 1000:
            # print(name, price, rating, rating_cnt)
            print(f"제품명: {name}")
            print(f"가격: {price}")
            print(f"평점: {rating}점 ({rating_cnt}개)")
            print('바로가기: {}'.format('https://coupang.com'+link))
            print("-"*100)  # 줄긋기
