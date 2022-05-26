from django.shortcuts import render
import requests

from the_weather.weather.forms import CityForm
from .models import City

# Create your views here.

def index(request):
    cities = City.objects.all()
    url = 'https://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=4af1395021b653043d98c4bacde91767'
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save
    form = CityForm()
    weather_data = []
    for city in cities:

        city_weather = requests.get(url.format(city)).json() # request the API data and convert the JSON to Python data types
        weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/index.html', context) #returns the index.html template