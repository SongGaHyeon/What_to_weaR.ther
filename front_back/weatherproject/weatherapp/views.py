from django.shortcuts import render
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import random
import os

# Create your views here.

i = random.randrange(0, 89)

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
one_subject = ''
one_address = ''
one_img = ''
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
    global  one_subject
    global  one_address
    global  one_img
    global  two_subject
    global  two_address
    global  two_img
    global  three_subject
    global  three_address
    global  three_img
    global  four_subject
    global  four_address
    global  four_img
    global  five_subject
    global  five_address
    global  five_img
    global  six_subject
    global  six_address
    global  six_img

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


def skirt():
    skirt_data = []
    f = open('templates/clothes/치마_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        skirt_data.append(line)

    f.close()
    return skirt_data[i]


def summer_pants():
    summerpants_data = []
    f = open('templates/clothes/여름바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        summerpants_data.append(line)

    f.close()
    return summerpants_data[i]


def short_sleeve():
    shortsleeve_data = []
    f = open('templates/clothes/반팔티_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        shortsleeve_data.append(line)

    f.close()
    return shortsleeve_data[i]


def short_shirts():
    shortshirts_data = []
    f = open('templates/clothes/반팔셔츠_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        shortshirts_data.append(line)

    f.close()
    return shortshirts_data[i]


def shorts():
    shorts_data = []
    f = open('templates/clothes/반바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        shorts_data.append(line)

    f.close()
    return shorts_data[i]


def sleeveless():
    sleeveless_data = []
    f = open('templates/clothes/민소매_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        sleeveless_data.append(line)

    f.close()
    return sleeveless_data[i]


def dress():
    dress_data = []
    f = open('templates/clothes/원피스_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        dress_data.append(line)

    f.close()
    return dress_data[i]


def shirts():
    shirts_data = []
    f = open('templates/clothes/셔츠_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        shirts_data.append(line)

    f.close()
    return shirts_data[i]


def long_sleeve():
    longsleeve_data = []
    f = open('templates/clothes/긴팔티_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        longsleeve_data.append(line)

    f.close()
    return longsleeve_data[i]


def seven_pants():
    sevenpants_data = []
    f = open('templates/clothes/7부바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        sevenpants_data.append(line)

    f.close()
    return sevenpants_data[i]


def bluejacket():
    bluejacket_data = []
    f = open('templates/clothes/청자켓_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        bluejacket_data.append(line)

    f.close()
    return bluejacket_data[i]


def thin_knit():
    thinknit_data = []
    f = open('templates/clothes/얇은니트_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        thinknit_data.append(line)

    f.close()
    return thinknit_data[i]


def slacks():
    slacks_data = []
    f = open('templates/clothes/슬랙스_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        slacks_data.append(line)

    f.close()
    return slacks_data[i]


def cotton_pants():
    cottonpants_data = []
    f = open('templates/clothes/면바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        cottonpants_data.append(line)

    f.close()
    return cottonpants_data[i]


def sweatshirt():
    sweatshirt_data = []
    f = open('templates/clothes/맨투맨_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        sweatshirt_data.append(line)

    f.close()
    return sweatshirt_data[i]


def cardigan():
    cardigan_data = []
    f = open('templates/clothes/가디건_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        cardigan_data.append(line)

    f.close()
    return cardigan_data[i]


def airlinejumper():
    airlinejumper_data = []
    f = open('templates/clothes/항공점퍼_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        airlinejumper_data.append(line)

    f.close()
    return airlinejumper_data[i]


def trenchcoat():
    trenchcoat_data = []
    f = open('templates/clothes/트렌치코트_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        trenchcoat_data.append(line)

    f.close()
    return trenchcoat_data[i]


def jean():
    jean_data = []
    f = open('templates/clothes/청바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        jean_data.append(line)

    f.close()
    return jean_data[i]


def fieldjumper():
    fieldjumper_data = []
    f = open('templates/clothes/야상_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        fieldjumper_data.append(line)

    f.close()
    return fieldjumper_data[i]


def knit():
    knit_data = []
    f = open('templates/clothes/니트_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        knit_data.append(line)

    f.close()
    return knit_data[i]


def furhood():
    furhood_data = []
    f = open('templates/clothes/기모후드티_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        furhood_data.append(line)

    f.close()
    return furhood_data[i]


def fleece():
    fleece_data = []
    f = open('templates/clothes/후리스_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        fleece_data.append(line)

    f.close()
    return fleece_data[i]


def shortpadding():
    shortpadding_data = []
    f = open('templates/clothes/숏패딩_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        shortpadding_data.append(line)

    f.close()
    return shortpadding_data[i]


def lightpadding():
    lightpadding_data = []
    f = open('templates/clothes/경량패딩_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        lightpadding_data.append(line)

    f.close()
    return lightpadding_data[i]


def leatherjacket():
    leatherjacket_data = []
    f = open('templates/clothes/가죽자켓_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        leatherjacket_data.append(line)

    f.close()
    return leatherjacket_data[i]


def winter_pants():
    pants_data = []
    f = open('templates/clothes/겨울바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        pants_data.append(line)

    f.close()
    return pants_data[i]

# 제목, 링크, 이미지src

    # [[]
    # []
    # []
    # []]


def coat():
    coat_data = []
    f = open('templates/clothes/두꺼운코트_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        coat_data.append(line)

    f.close()
    return coat_data[i]


def muffler():
    muffler_data = []
    f = open('templates/clothes/목도리_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        muffler_data.append(line)

    f.close()
    return muffler_data[i]


def glove():
    glove_data = []
    f = open('templates/clothes/장갑_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        glove_data.append(line)

    f.close()
    return glove_data[i]


def padding():
    padding_data = []
    f = open('templates/clothes/패딩_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        padding_data.append(line)

    f.close()
    return padding_data[i]


def heat():
    heat_data = []
    f = open('templates/clothes/히트텍_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        heat_data.append(line)

    f.close()
    return heat_data[i]


# ▼ 자기가 맡은 온도에 있는 옷 같이 구현 -> 중복된 옷이면 안해도 됨


# def 두꺼운 코트():
#     coat_data=[]
#     f = open('두꺼운코트_data.csv', 'r')
#     rdr = csv.reader(f)

#     for line in rdr:
#         coat_data.append(line)

#     f.close()
#     return ~~


def index(request):
    city = 'Seoul'
    appid = '0de8ed3564750bc9221f0e10a4a2031d'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q': city, 'appid': appid, 'units': 'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']

    if temp < 5:
        minus4()
    elif 5 <= temp < 9:
        five_eight()
    elif 9 <= temp < 15:
        nine_fourteen()
    elif 15 <= temp < 20:
        fifteen_nineteen()
    elif 20 <= temp < 24:
        twenty_twentythree()
    elif 24 <= temp:
        plus24()


    return render(request, 'weatherapp/index.html', {'icon': icon, 'temp': temp,
                                                     'one_subject': one_subject, 'two_subject': two_subject, 'three_subject': three_subject, 'four_subject': four_subject, 'five_subject': five_subject, 'six_subject': six_subject,
                                                     'one_address': one_address, 'two_address': two_address, 'three_address': three_address, 'four_address': four_address, 'five_address': five_address, 'six_address': six_address,
                                                     'one_img': one_img, 'two_img': two_img, 'three_img': three_img, 'four_img': four_img, 'five_img': five_img, 'six_img': six_img, })