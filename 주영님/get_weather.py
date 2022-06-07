import requests
import json
import math

city_name = "Seoul,KR"
api_key = "0de8ed3564750bc9221f0e10a4a2031d"

# 캘빈 온도 -> 섭씨 온도
k2c = lambda x: x - 273.15

def get_weather(api_key,city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = json.loads(response.text)
    #print(data)
    print("도시 =", data["name"])
    print("날씨 =", data["weather"][0]["description"])
    print("최저 기온 =", math.floor(k2c(data["main"]["temp_min"])))
    print("최고 기온 =", math.floor(k2c(data["main"]["temp_max"])))
    

get_weather(api_key,city_name)
