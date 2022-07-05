from selenium import webdriver
import time
browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get('https://naver.com')

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name('link_login')
elem.click()

# 3. 아이디&비밀번호 입력
browser.find_element_by_id('id').send_keys('bungaedm')
browser.find_element_by_id('pw').send_keys('0000')

# 4. 로그인 버튼 클릭
browser.find_element_by_id('log.login').click()

# 5. ID 다시 입력
time.sleep(3)
browser.find_element_by_id('id').clear()
browser.find_element_by_id('id').send_keys('new_id')

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료
