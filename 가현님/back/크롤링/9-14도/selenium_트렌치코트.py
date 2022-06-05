from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('C:/chromedriver.exe')
browser.get('https://www.musinsa.com/app/')
browser.implicitly_wait(3)

search = browser.find_element_by_css_selector('input.search.head-search-inp')
search.click()

search.send_keys('트렌치코트')
search.send_keys(Keys.ENTER)

time.sleep(2)

# ..
browser.execute_script('window.scrollTo(0, 2000)')
time.sleep(2)

products = browser.find_element_by_css_selector('a.btn-all.font-mss')
products.click()


# scrolling
before_h = browser.execute_script("return window.scrollY")
while True:
    # To END : 전 높이 (before_h) /후 높이
    browser.find_element_by_css_selector("body").send_keys(Keys.END)
    time.sleep(1)

    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

items = browser.find_elements_by_css_selector("#searchList li.li_box")

for item in items:
    title = item.find_element_by_css_selector(
        ".list_img > a").get_attribute('title')
    print(title)
    link = item.find_element_by_css_selector(
        ".list_img > a").get_attribute('href')
    print(link)
