from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('https://www.naver.com')

# Class (뒤로가기, 새로고침 등)
elem = browser.find_element_by_class_name('link_login')
elem
elem.click()
browser.back()
browser.forward()
browser.refresh()
browser.back()

# ID (입력 및 ENTER키 누르기)
elem = browser.find_element_by_id('query')
elem.send_keys('나도코딩')
elem.send_keys(Keys.ENTER)
elem.clear()

# Tag
elem = browser.find_elements_by_tag_name('a')
for e in elem:
    e.get_attribute('href')

# Name
elem = browser.find_element_by_name('q')

# Xpath
elem = browser.find_element_by_xpath(
    '//*[@id="web_2"]/div/div[2]/div[2]/a/mark')
elem.click()

# 브라우저 닫기
browser.quit()
