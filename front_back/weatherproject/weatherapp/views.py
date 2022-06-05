from django.shortcuts import render
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import random

# Create your views here.

i = random.randrange(0,89)


def winter_pants():
    pants_data = []
    f = open('겨울바지_data.csv', 'r')
    rdr = csv.reader(f)

    for line in rdr:
        pants_data.append(line)



    f.close()




def index(request):
    city = 'Seoul'
    appid = '0de8ed3564750bc9221f0e10a4a2031d'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']




    return render(request, 'weatherapp/index.html', {'icon':icon, 'temp':temp, 'city':city, 'subject': , 'address': b, 'img': c})