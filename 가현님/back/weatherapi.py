import requests
import json

city = "Seoul"  # 도시
apiKey = "144bb9d4aba3215ac058a8c899ea0188"
lang = 'kr'  # 언어
units = 'metric'  # 화씨 온도를 섭씨 온도로 변경
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

result = requests.get(api)
result = json.loads(result.text)

print(result)
