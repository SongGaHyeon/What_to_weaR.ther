from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Seoul'
    appid = '0de8ed3564750bc9221f0e10a4a2031d'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':city, 'appid':appid, 'units':'metric'}
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    icon = res['weather'][0]['icon']
    temp_min = res['main']['temp_min']
    temp_max = res['main']['temp_max']
    return render(request, 'weatherapp/index.html', {'icon':icon, 'temp_min':temp_min, 'temp_max':temp_max, 'city':city})