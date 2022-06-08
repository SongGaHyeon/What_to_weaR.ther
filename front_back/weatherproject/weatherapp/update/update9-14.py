from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv


def furhood():
    browser = webdriver.Chrome('C:/chromedriver.exe')
    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('기모 후드티')
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

    f = open(r"기모후드티_data.csv", 'w', encoding='CP949', newline='')
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


def knit():
    browser = webdriver.Chrome('C:/chromedriver.exe')
    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('니트')
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

    f = open(r"니트_data.csv", 'w', encoding='CP949', newline='')
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


def fjacket():
    browser = webdriver.Chrome('C:/chromedriver.exe')

    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('야상')
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

    f = open(r"야상_data.csv", 'w', encoding='CP949', newline='')
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


def jeans():
    browser = webdriver.Chrome('C:/chromedriver.exe')

    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('청바지')
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

    f = open(r"청바지_data.csv", 'w', encoding='CP949', newline='')
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


def trench():
    browser = webdriver.Chrome('C:/chromedriver.exe')

    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
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

    f = open(r"트렌치코트_data.csv", 'w', encoding='CP949', newline='')
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


def airline():
    browser = webdriver.Chrome('C:/chromedriver.exe')

    browser.get('https://www.musinsa.com/app/')
    browser.implicitly_wait(3)

    search = browser.find_element_by_css_selector(
        'input.search.head-search-inp')
    search.click()

    search.send_keys('항공점퍼')
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

    f = open(r"항공점퍼_data.csv", 'w', encoding='CP949', newline='')
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


def mojori():
    furhood()
    knit()
    fjacket()
    jeans()
    trench()
    airline()


mojori()
