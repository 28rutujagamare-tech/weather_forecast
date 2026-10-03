from django.shortcuts import render
import requests
from django.contrib import messages
import os
from dotenv import load_dotenv
# Create your views here.
load_dotenv()

def weather(request):
    if request.method == 'POST':
        api_key = os.getenv('OPENWEATHER_API_KEY')
        base_url = 'https://api.openweathermap.org/data/2.5/weather'

        city = request.POST.get('city')
        params = {
            'q': city,
            'appid': api_key
        }

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity'],
            }
            return render(request,'weather_data.html',weather_data)
        elif response.status_code == 404:
            if not response: 
                messages.error(request, "City not found")
        elif response.status_code == 401:
            if not response: 
                messages.error(request, "Invalid API key")
        else:
            messages.error(request, "Something went wrong")
   

    return render(request, 'form.html')