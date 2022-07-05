from selenium import webdriver
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')
browser = webdriver.Chrome(options=options)

# 페이지 이동
url = 'https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA&hl=ko&gl=US'
browser.get(url)

# 지정한 위치로 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0,1080)')

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
interval = 2  # 2초에 한 번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# 반복 수행
while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(interval)
    cur_height = browser.execute_script('return document.body.scrollHeight')

    if cur_height == prev_height:
        break

    prev_height = cur_height


soup = BeautifulSoup(browser.page_source, 'lxml')

movies = soup.find_all('div', attrs={'class': 'Vpfmgd'})
for idx, movie in enumerate(movies):
    discount = movie.find('span', attrs={'class': 'SUZt4c djCuy'})
    if discount:
        title = movie.find('div', attrs={'class': 'WsMG1c nnK0zc'}).get_text()
        print(idx+1, ": ", title, sep='')

browser.get_screenshot_as_file('gmovie.png')  # 확인용 스크린샷
