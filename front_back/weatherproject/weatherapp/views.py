import os

from django.shortcuts import render
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import random

# Create your views here.

i = 0
'''
요부분 전체적으로 추가해주세요
레퍼런스 thinknit()

if len(thinknit_data) < i:
    j = i % len(thinknit_data)
else: j = i
'''


# 4도 이하, 5-8도 -> 가현
# 9-14도 + 9-14에 맞는 옷 엑셀 배열로 저장하는 부분-> 희원
# 15-19도 -> 희원
# 20-23도 -> 희원

a = []
b = []
c = []
d = []
e = []
f = []
one_subject = os.getcwd()
one_address = '2'
one_img = '3'
two_subject = ''
two_address = ''
two_img = ''
three_subject = ''
three_address = ''
three_img = ''
four_subject = ''
four_address = ''
four_img = ''
five_subject = ''
five_address = ''
five_img = ''
six_subject = ''
six_address = ''
six_img = ''
# -------------------------------------------------------
# 4도 이하


def minus4():
    global a, b, c, d, e, f
    global one_subject
    global one_address
    global one_img
    global two_subject
    global two_address
    global two_img
    global three_subject
    global three_address
    global three_img
    global four_subject
    global four_address
    global four_img
    global five_subject
    global five_address
    global five_img
    global six_subject
    global six_address
    global six_img

    a = winter_pants()
    one_subject = a[0]
    one_address = a[1]
    one_img = a[2]

    b = coat()
    two_subject = b[0]
    two_address = b[1]
    two_img = b[2]

    c = muffler()
    three_subject = c[0]
    three_address = c[1]
    three_img = c[2]

    d = glove()
    four_subject = d[0]
    four_address = d[1]
    four_img = d[2]

    e = padding()
    five_subject = e[0]
    five_address = e[1]
    five_img = e[2]

    f = heat()
    six_subject = f[0]
    six_address = f[1]
    six_img = f[2]

# ----------------------------------------------
# 5-8도


def five_eight():
    global a, b, c, d, e, f
    global one_subject
    global one_address
    global one_img
    global two_subject
    global two_address
    global two_img
    global three_subject
    global three_address
    global three_img
    global four_subject
    global four_address
    global four_img
    global five_subject
    global five_address
    global five_img
    global six_subject
    global six_address
    global six_img
    a = leatherjacket()
    one_subject = a[0]
    one_address = a[1]
    one_img = a[2]

    b = lightpadding()
    two_subject = b[0]
    two_address = b[1]
    two_img = b[2]

    c = shortpadding()
    three_subject = c[0]
    three_address = c[1]
    three_img = c[2]

    d = coat()  # 옷이 위에와 중복됨
    four_subject = d[0]
    four_address = d[1]
    four_img = d[2]

    e = fleece()
    five_subject = e[0]
    five_address = e[1]
    five_img = e[2]

    f = heat()  # 옷이 위에와 중복됨
    six_subject = f[0]
    six_address = f[1]
    six_img = f[2]

# ----------------------------------------------
# 9-14도


def nine_fourteen():
    global a, b, c, d, e, f
    global one_subject
    global one_address
    global one_img
    global two_subject
    global two_address
    global two_img
    global three_subject
    global three_address
    global three_img
    global four_subject
    global four_address
    global four_img
    global five_subject
    global five_address
    global five_img
    global six_subject
    global six_address
    global six_img
    a = furhood()
    one_subject = a[0]
    one_address = a[1]
    one_img = a[2]

    b = knit()
    two_subject = b[0]
    two_address = b[1]
    two_img = b[2]

    c = fieldjumper()
    three_subject = c[0]
    three_address = c[1]
    three_img = c[2]

    d = jean()
    four_subject = d[0]
    four_address = d[1]
    four_img = d[2]

    e = trenchcoat()
    five_subject = e[0]
    five_address = e[1]
    five_img = e[2]

    f = airlinejumper()
    six_subject = f[0]
    six_address = f[1]
    six_img = f[2]

# -------------------------------------------------------
#  15-19도


def fifteen_nineteen():
    global a, b, c, d, e, f
    global one_subject
    global one_address
    global one_img
    global two_subject
    global two_address
    global two_img
    global three_subject
    global three_address
    global three_img
    global four_subject
    global four_address
    global four_img
    global five_subject
    global five_address
    global five_img
    global six_subject
    global six_address
    global six_img
    a = cardigan()
    one_subject = a[0]
    one_address = a[1]
    one_img = a[2]

    b = sweatshirt()
    two_subject = b[0]
    two_address = b[1]
    two_img = b[2]

    c = cotton_pants()
    three_subject = c[0]
    three_address = c[1]
    three_img = c[2]

    d = slacks()
    four_subject = d[0]
    four_address = d[1]
    four_img = d[2]

    e = thin_knit()
    five_subject = e[0]
    five_address = e[1]
    five_img = e[2]

    f = bluejacket()
    six_subject = f[0]
    six_address = f[1]
    six_img = f[2]

# -------------------------------------------------------
# 20-23도


def twenty_twentythree():
    global a, b, c, d, e, f
    global one_subject
    global one_address
    global one_img
    global two_subject
    global two_address
    global two_img
    global three_subject
    global three_address
    global three_img
    global four_subject
    global four_address
    global four_img
    global five_subject
    global five_address
    global five_img
    global six_subject
    global six_address
    global six_img
    a = seven_pants()
    one_subject = a[0]
    one_address = a[1]
    one_img = a[2]

    b = long_sleeve()
    two_subject = b[0]
    two_address = b[1]
    two_img = b[2]

    c = cotton_pants()
    three_subject = c[0]
    three_address = c[1]
    three_img = c[2]

    d = shirts()
    four_subject = d[0]
    four_address = d[1]
    four_img = d[2]

    e = slacks()
    five_subject = e[0]
    five_address = e[1]
    five_img = e[2]

    f = dress()
    six_subject = f[0]
    six_address = f[1]
    six_img = f[2]

# -------------------------------------------------------
# 24도 이상


def plus24():
    global a, b, c, d, e, f
    global one_subject
    global one_address
    global one_img
    global two_subject
    global two_address
    global two_img
    global three_subject
    global three_address
    global three_img
    global four_subject
    global four_address
    global four_img
    global five_subject
    global five_address
    global five_img
    global six_subject
    global six_address
    global six_img
    a = sleeveless()
    one_subject = a[0]
    one_address = a[1]
    one_img = a[2]

    b = shorts()
    two_subject = b[0]
    two_address = b[1]
    two_img = b[2]

    c = short_shirts()
    three_subject = c[0]
    three_address = c[1]
    three_img = c[2]

    d = short_sleeve()
    four_subject = d[0]
    four_address = d[1]
    four_img = d[2]

    e = summer_pants()
    five_subject = e[0]
    five_address = e[1]
    five_img = e[2]

    f = skirt()
    six_subject = f[0]
    six_address = f[1]
    six_img = f[2]

# -------------------------------------------------------
# 옷별 함수

# [옷제목, 링크, src]


def skirt():
    skirt_data = []

    f = open("./weatherapp/static\clothes\치마_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        skirt_data.append(line)

    f.close()

    if len(skirt_data) < i:
        j = i % len(skirt_data)
    else:
        j = i
    return skirt_data[j]


def summer_pants():
    summerpants_data = []

    f = open("./weatherapp/static/clothes/여름바지_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        summerpants_data.append(line)

    f.close()

    if len(summerpants_data) < i:
        j = i % len(summerpants_data)
    else:
        j = i
    return summerpants_data[j]


def short_sleeve():
    shortsleeve_data = []

    f = open("./weatherapp/static/clothes/반팔티_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        shortsleeve_data.append(line)

    f.close()

    if len(shortsleeve_data) < i:
        j = i % len(shortsleeve_data)
    else:
        j = i
    return shortsleeve_data[j]


def short_shirts():
    shortshirts_data = []

    f = open("./weatherapp/static/clothes/반팔셔츠_data.csv", 'r')
    rdr = csv.reader(f)

    for line in rdr:
        shortshirts_data.append(line)

    f.close()

    if len(shortshirts_data) < i:
        j = i % len(shortshirts_data)
    else:
        j = i
    return shortshirts_data[j]


def shorts():
    shorts_data = []

    f = open("./weatherapp/static/clothes/반바지_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        shorts_data.append(line)

    f.close()

    if len(shorts_data) < i:
        j = i % len(shorts_data)
    else:
        j = i
    return shorts_data[j]


def sleeveless():
    sleeveless_data = []

    f = open("./weatherapp/static/clothes/민소매_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        sleeveless_data.append(line)

    f.close()

    if len(sleeveless_data) < i:
        j = i % len(sleeveless_data)
    else:
        j = i
    return sleeveless_data[j]


def dress():
    dress_data = []

    f = open("./weatherapp/static/clothes/원피스_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        dress_data.append(line)

    f.close()

    if len(dress_data) < i:
        j = i % len(dress_data)
    else:
        j = i
    return dress_data[j]


def shirts():
    shirts_data = []

    f = open("./weatherapp/static/clothes/셔츠_data.csv", 'r')
    rdr = csv.reader(f)

    for line in rdr:
        shirts_data.append(line)

    f.close()

    if len(shirts_data) < i:
        j = i % len(shirts_data)
    else:
        j = i
    return shirts_data[j]


def long_sleeve():
    longsleeve_data = []
    f = open("./weatherapp/static/clothes/긴팔티_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        longsleeve_data.append(line)

    f.close()

    if len(longsleeve_data) < i:
        j = i % len(longsleeve_data)
    else:
        j = i
    return longsleeve_data[j]


def seven_pants():
    sevenpants_data = []

    f = open("./weatherapp/static/clothes/칠부바지_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        sevenpants_data.append(line)

    f.close()

    if len(sevenpants_data) < i:
        j = i % len(sevenpants_data)
    else:
        j = i
    return sevenpants_data[j]


def bluejacket():
    bluejacket_data = []

    f = open("./weatherapp/static/clothes/청자켓_data.csv", 'r')
    rdr = csv.reader(f)

    for line in rdr:
        bluejacket_data.append(line)

    f.close()

    if len(bluejacket_data) < i:
        j = i % len(bluejacket_data)
    else:
        j = i
    return bluejacket_data[j]


def thin_knit():
    thinknit_data = []

    f = open("./weatherapp/static/clothes/얇은니트_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        thinknit_data.append(line)

    f.close()

    if len(thinknit_data) < i:
        j = i % len(thinknit_data)
    else:
        j = i

    if len(thinknit_data) < i:
        j = i % len(thinknit_data)
    else:
        j = i
    return thinknit_data[j]


def slacks():
    slacks_data = []

    f = open("./weatherapp/static/clothes/슬랙스_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        slacks_data.append(line)

    f.close()

    if len(slacks_data) < i:
        j = i % len(slacks_data)
    else:
        j = i
    return slacks_data[j]


def cotton_pants():
    cottonpants_data = []

    f = open("./weatherapp/static/clothes/면바지_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        cottonpants_data.append(line)

    f.close()

    if len(cottonpants_data) < i:
        j = i % len(cottonpants_data)
    else:
        j = i
    return cottonpants_data[j]


def sweatshirt():
    sweatshirt_data = []

    f = open("./weatherapp/static/clothes/맨투맨_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        sweatshirt_data.append(line)

    f.close()

    if len(sweatshirt_data) < i:
        j = i % len(sweatshirt_data)
    else:
        j = i
    return sweatshirt_data[j]


def cardigan():
    cardigan_data = []

    f = open("./weatherapp/static/clothes/가디건_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        cardigan_data.append(line)

    f.close()

    if len(cardigan_data) < i:
        j = i % len(cardigan_data)
    else:
        j = i
    return cardigan_data[j]


def airlinejumper():
    airlinejumper_data = []

    f = open("./weatherapp/static/clothes/항공점퍼_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        airlinejumper_data.append(line)

    f.close()

    if len(airlinejumper_data) < i:
        j = i % len(airlinejumper_data)
    else:
        j = i
    return airlinejumper_data[j]


def trenchcoat():
    trenchcoat_data = []

    f = open("./weatherapp/static/clothes/트렌치코트_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        trenchcoat_data.append(line)

    f.close()

    if len(trenchcoat_data) < i:
        j = i % len(trenchcoat_data)
    else:
        j = i
    return trenchcoat_data[j]


def jean():
    jean_data = []

    f = open("./weatherapp/static/clothes/청바지_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        jean_data.append(line)

    f.close()

    if len(jean_data) < i:
        j = i % len(jean_data)
    else:
        j = i
    return jean_data[j]


def fieldjumper():
    fieldjumper_data = []

    f = open("./weatherapp/static/clothes/야상_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        fieldjumper_data.append(line)

    f.close()

    if len(fieldjumper_data) < i:
        j = i % len(fieldjumper_data)
    else:
        j = i
    return fieldjumper_data[j]


def knit():
    knit_data = []

    f = open("./weatherapp/static/clothes/니트_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        knit_data.append(line)

    f.close()

    if len(knit_data) < i:
        j = i % len(knit_data)
    else:
        j = i
    return knit_data[j]


def furhood():
    furhood_data = []

    f = open("./weatherapp/static/clothes/기모후드티_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        furhood_data.append(line)

    f.close()

    if len(furhood_data) < i:
        j = i % len(furhood_data)
    else:
        j = i
    return furhood_data[j]


def fleece():
    fleece_data = []

    f = open("./weatherapp/static/clothes/후리스_data.csv", 'r')
    rdr = csv.reader(f)

    for line in rdr:
        fleece_data.append(line)

    f.close()

    if len(fleece_data) < i:
        j = i % len(fleece_data)
    else:
        j = i
    return fleece_data[j]


def shortpadding():
    shortpadding_data = []
    f = open("./weatherapp/static/clothes/숏패딩_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        shortpadding_data.append(line)

    f.close()

    if len(shortpadding_data) < i:
        j = i % len(shortpadding_data)
    else:
        j = i
    return shortpadding_data[j]


def lightpadding():
    lightpadding_data = []

    f = open("./weatherapp/static/clothes/경량패딩_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        lightpadding_data.append(line)

    f.close()

    if len(lightpadding_data) < i:
        j = i % len(lightpadding_data)
    else:
        j = i
    return lightpadding_data[j]


def leatherjacket():
    leatherjacket_data = []

    f = open("./weatherapp/static/clothes/가죽자켓_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        leatherjacket_data.append(line)

    f.close()

    if len(leatherjacket_data) < i:
        j = i % len(leatherjacket_data)
    else:
        j = i
    return leatherjacket_data[j]


def winter_pants():
    pants_data = []

    f = open("./weatherapp/static/clothes/겨울바지_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        pants_data.append(line)

    f.close()

    if len(pants_data) < i:
        j = i % len(pants_data)
    else:
        j = i
    return pants_data[j]

# 제목, 링크, 이미지src

    # [[]
    # []
    # []
    # []]


def coat():
    coat_data = []

    f = open("./weatherapp/static/clothes/두꺼운코트_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        coat_data.append(line)

    f.close()

    if len(coat_data) < i:
        j = i % len(coat_data)
    else:
        j = i
    return coat_data[j]


def muffler():
    muffler_data = []

    f = open("./weatherapp/static/clothes/목도리_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        muffler_data.append(line)

    f.close()

    if len(muffler_data) < i:
        j = i % len(muffler_data)
    else:
        j = i
    return muffler_data[j]


def glove():
    glove_data = []

    f = open("./weatherapp/static/clothes/장갑_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        glove_data.append(line)

    f.close()

    if len(glove_data) < i:
        j = i % len(glove_data)
    else:
        j = i
    return glove_data[j]


def padding():
    padding_data = []

    f = open("./weatherapp/static/clothes/패딩_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        padding_data.append(line)

    f.close()

    if len(padding_data) < i:
        j = i % len(padding_data)
    else:
        j = i
    return padding_data[j]


def heat():
    heat_data = []

    f = open("./weatherapp/static/clothes/히트텍_data.csv", 'r')

    rdr = csv.reader(f)

    for line in rdr:
        heat_data.append(line)

    f.close()

    if len(heat_data) < i:
        j = i % len(heat_data)
    else:
        j = i
    return heat_data[j]


# ▼ 자기가 맡은 온도에 있는 옷 같이 구현 -> 중복된 옷이면 안해도 됨


# def 두꺼운 코트():
#     coat_data=[]
#     f = open('두꺼운코트_data.csv", 'r')
#     rdr = csv.reader(f)

#     for line in rdr:
#         coat_data.append(line)

#     f.close()
#     return ~~


def index(request):
    global i
    i = random.randrange(0, 89)
    city = 'Seoul'
    appid = '0de8ed3564750bc9221f0e10a4a2031d'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']

    if temp <= 4:
        minus4()
    elif temp <= 8:
        five_eight()
    elif 8 < temp <= 14:
        nine_fourteen()
    elif 14 < temp <= 19:
        fifteen_nineteen()
    elif 19 < temp <= 23:
        twenty_twentythree()
    else:
        plus24()

    return render(request, './weatherapp/index.html',
                  {'icon': icon, 'temp': temp, 'city': city,
                   'one_subject': one_subject, 'two_subject': two_subject, 'three_subject': three_subject, 'four_subject': four_subject, 'five_subject': five_subject, 'six_subject': six_subject,
                   'one_address': one_address, 'two_address': two_address, 'three_address': three_address, 'four_address': four_address, 'five_address': five_address, 'six_address': six_address,
                   'one_img': one_img, 'two_img': two_img, 'three_img': three_img, 'four_img': four_img, 'five_img': five_img, 'six_img': six_img, })
