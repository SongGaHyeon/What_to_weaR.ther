from django.shortcuts import render
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import random

# Create your views here.

i = random.randrange(0, 89)

# 4도 이하, 5-8도 -> 가현
# 9-14도 + 9-14에 맞는 옷 엑셀 배열로 저장하는 부분-> 희원
# 15-19도 -> 주영
# 20-23도 -> 주희

a = []
b = []
c = []
d = []
e = []
f = []

# -------------------------------------------------------
# 4도 이하


def minus4():
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
    a = cardigan()
    one_subject = a[0]
    one = a[1]
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


# -------------------------------------------------------
# 옷별 함수

def bluejacket():
    bluejacket_data = []
    f = open('청자켓_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        bluejacket_data.append(line)

    f.close()
    return bluejacket_data[i]

def thin_knit():
    thinknit_data = []
    f = open('얇은니트_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        thinknit_data.append(line)

    f.close()
    return thinknit_data[i]

def slacks():
    slacks_data = []
    f = open('슬랙스_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        slacks_data.append(line)

    f.close()
    return slacks_data[i]

def cotton_pants():
    cottonpants_data = []
    f = open('면바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        cottonpants_data.append(line)

    f.close()
    return cottonpants_data[i]

def sweatshirt():
    sweatshirt_data = []
    f = open('맨투맨_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        sweatshirt_data.append(line)

    f.close()
    return sweatshirt_data[i]

def cardigan():
    cardigan_data = []
    f = open('가디건_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        cardigan_data.append(line)

    f.close()
    return cardigan_data[i]

def airlinejumper():
    airlinejumper_data = []
    f = open('항공점퍼_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        airlinejumper_data.append(line)

    f.close()
    return airlinejumper_data[i]


def trenchcoat():
    trenchcoat_data = []
    f = open('트렌치코트_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        trenchcoat_data.append(line)

    f.close()
    return trenchcoat_data[i]


def jean():
    jean_data = []
    f = open('청바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        jean_data.append(line)

    f.close()
    return jean_data[i]


def fieldjumper():
    fieldjumper_data = []
    f = open('야상_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        fieldjumper_data.append(line)

    f.close()
    return fieldjumper_data[i]


def knit():
    knit_data = []
    f = open('니트_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        knit_data.append(line)

    f.close()
    return knit_data[i]


def furhood():
    furhood_data = []
    f = open('기모후드티_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        furhood_data.append(line)

    f.close()
    return furhood_data[i]


def fleece():
    fleece_data = []
    f = open('후리스_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        fleece_data.append(line)

    f.close()
    return fleece_data[i]


def shortpadding():
    shortpadding_data = []
    f = open('숏패딩_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        shortpadding_data.append(line)

    f.close()
    return shortpadding_data[i]


def lightpadding():
    lightpadding_data = []
    f = open('경량패딩_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        lightpadding_data.append(line)

    f.close()
    return lightpadding_data[i]


def leatherjacket():
    leatherjacket_data = []
    f = open('가죽자켓_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        leatherjacket_data.append(line)

    f.close()
    return leatherjacket_data[i]


def winter_pants():
    pants_data = []
    f = open('겨울바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        pants_data.append(line)

    f.close()
    return pants_data[i]


def coat():
    coat_data = []
    f = open('두꺼운코트_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        coat_data.append(line)

    f.close()
    return coat_data[i]


def muffler():
    muffler_data = []
    f = open('목도리_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        muffler_data.append(line)

    f.close()
    return muffler_data[i]


def glove():
    glove_data = []
    f = open('장갑_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        glove_data.append(line)

    f.close()
    return glove_data[i]


def padding():
    padding_data = []
    f = open('패딩_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        padding_data.append(line)

    f.close()
    return padding_data[i]


def heat():
    heat_data = []
    f = open('히트텍_data.csv', 'r')
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

    return render(request, 'weatherapp/index.html', {'icon': icon, 'temp': temp, 'one_subject': a[0], 'two_subject': b[0], 'three_subject': c[0], 'four_subject': d[0], 'five_subject': e[0], 'six_subject': f[0], 'one_address': a[1], 'two_address': b[1], 'three_address': c[1], 'four_address': d[1], 'five_address': e[1], 'six_address': f[1], 'one_img': a[2], 'two_img': b[2], 'three_img': c[2], 'four_img': d[2], 'five_img': e[2], 'six_img': f[2], })
