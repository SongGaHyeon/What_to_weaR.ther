from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


def min():

    browser = webdriver.Chrome('C:/chromedriver.exe')
    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('민소매')
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

    f = open(r"민소매_data.csv", 'w', encoding='CP949', newline='')
    csvWriter = csv.writer(f)
    items = browser.find_elements_by_css_selector("#searchList li.li_box")

    for item in items:
        title = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('title')
        print(title)
        link = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('href')
        print(link)
        image = item.find_element_by_css_selector(
            ".lazyload.lazy").get_attribute('data-original')
        print(image)
        csvWriter.writerow([title, link, image])


def banbaji():
    browser = webdriver.Chrome('C:/chromedriver.exe')

    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('반바지')
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

    f = open(r"반바지_data.csv", 'w', encoding='CP949', newline='')
    csvWriter = csv.writer(f)
    items = browser.find_elements_by_css_selector("#searchList li.li_box")

    for item in items:
        title = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('title')
        print(title)
        link = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('href')
        print(link)
        image = item.find_element_by_css_selector(
            ".lazyload.lazy").get_attribute('data-original')
        print(image)
        csvWriter.writerow([title, link, image])


def banshirt():
    browser = webdriver.Chrome('C:/chromedriver.exe')

    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('반팔셔츠')
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

    f = open(r"반팔셔츠_data.csv", 'w', encoding='CP949', newline='')
    csvWriter = csv.writer(f)
    items = browser.find_elements_by_css_selector("#searchList li.li_box")

    for item in items:
        title = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('title')
        print(title)
        link = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('href')
        print(link)
        image = item.find_element_by_css_selector(
            ".lazyload.lazy").get_attribute('data-original')
        print(image)
        csvWriter.writerow([title, link, image])


def bant():
    browser = webdriver.Chrome('C:/chromedriver.exe')
    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('반팔티')
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

    f = open(r"반팔티_data.csv", 'w', encoding='CP949', newline='')
    csvWriter = csv.writer(f)
    items = browser.find_elements_by_css_selector("#searchList li.li_box")

    for item in items:
        title = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('title')
        print(title)
        link = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('href')
        print(link)
        image = item.find_element_by_css_selector(
            ".lazyload.lazy").get_attribute('data-original')
        print(image)

        csvWriter.writerow([title, link, image])


def summerbaji():
    browser = webdriver.Chrome('C:/chromedriver.exe')
    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('여름 바지')
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

    f = open(r"여름바지_data.csv", 'w', encoding='CP949', newline='')
    csvWriter = csv.writer(f)
    items = browser.find_elements_by_css_selector("#searchList li.li_box")

    for item in items:
        title = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('title')
        print(title)
        link = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('href')
        print(link)
        image = item.find_element_by_css_selector(
            ".lazyload.lazy").get_attribute('data-original')
        print(image)
        csvWriter.writerow([title, link, image])


def skirt():
    browser = webdriver.Chrome('C:/chromedriver.exe')
    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('치마')
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

    f = open(r"치마_data.csv", 'w', encoding='CP949', newline='')
    csvWriter = csv.writer(f)
    items = browser.find_elements_by_css_selector("#searchList li.li_box")

    for item in items:
        title = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('title')
        print(title)
        link = item.find_element_by_css_selector(
            ".list_img > a").get_attribute('href')
        print(link)
        image = item.find_element_by_css_selector(
            ".lazyload.lazy").get_attribute('data-original')
        print(image)
        csvWriter.writerow([title, link, image])


def mozori():
    min()
    banbaji()
    banshirt()
    bant()
    summerbaji()
    skirt()


mozori()
