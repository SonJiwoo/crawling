from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()  # 창 최대화
url = 'https://flight.naver.com'
browser.get(url)
time.sleep(3)

# 가는 날 클릭
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)

# 이번달 25일, 26일 선택
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button/b').click()
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button/b').click()

# 목적지 설정(제주도)
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b').click()
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[9]/div[1]/div/input').send_keys('제주')
elem = WebDriverWait(browser, 5).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a/div[1]/i[1]')))  # 조건부로 최대 5초 기다리기
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/div/a/div[1]/i[1]').click()

# 항공권 검색
browser.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div[4]/div/div/button/span').click()
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button')))  # 조건부로 최대 10초 기다리기
    print(elem.text)  # 첫번째 결과 출력
finally:
    browser.quit()
