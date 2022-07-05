import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # 처음으로 발견되는 a를 출력해줘
# print(soup.a.attrs)
# print(soup.find('a', attrs={'class': 'Nbtn_upload'}).get_text())

rank1 = soup.find('li', attrs={'class': 'rank01'})
# print(rank1.a.get_text())
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling # tip: 때에 따라서는 두 번 next_sibling을 해줘야하는 경우가 있다. 왜냐하면 빈 행이 있을 수도 있기 때문이다.
# rank3 = rank2.next_sibling.next_sibling
# print('2위:', rank2.a.get_text())
# print('3위:', rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print('2위:', rank2.a.get_text())

# print(rank1.parent)

# rank2 = rank1.find_next_sibling('li')
# rank3 = rank2.find_next_sibling('li')
# print(rank3.a.get_text())

print(rank1.find_next_siblings('li'))
