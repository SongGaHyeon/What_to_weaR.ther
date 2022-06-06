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
# 9-14도 -> 희원
# 15-19도 -> 주영
# 20-23도 -> 주희


# def -4이하():
#     a=winter_pants()
#     1_subject=a[0]
#     1_address=a[1]
#     1_img=a[2]

#     b=coat_data()
#     2_subject = b[0]
#     2_address = b[1]
#     2_img = b[2]

#     c=

#     d=

#     e=

#     f=

#     ..등등 6가지


# def 5~8():
#     위랑 같은 방식으로


def winter_pants():
    pants_data = []
    f = open('겨울바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        pants_data.append(line)

    f.close()
    return pants_data[i]


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

    return render(request, 'weatherapp/index.html', {'icon': icon, 'temp': temp,
                                                     '1_subject' : a[0], '2_subject' : b[0], '3_subject' : c[0], '4_subject' : d[0], '5_subject' : e[0], '6_subject' : f[0],
                                                     '1_address' : a[1], '2_address' : b[1], '3_address' : c[1], '4_address' : d[1], '5_address' : e[1], '6_address' : f[1],
                                                     '1_img' : a[0], '2_img' : b[0], '3_img' : c[0], '4_img' : d[0], '5_img' : e[0], '6_img' : f[0],})
    # 1_subject, 2_subject, ~~6_subject
    # 1_address, ......~~6_address
    # 1_img,..., 2_sub
    # 예찬님
