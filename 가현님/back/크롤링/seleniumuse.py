from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get('https://www.musinsa.com/app/')
browser.implicitly_wait(10)

search = browser.find_element_by_css_selector('input.search.head-search-inp')
search.click()

search.send_keys('가디건')
search.send_keys(Keys.ENTER)
