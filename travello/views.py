from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination


def index(request):
    dest1 = Destination()
    dest1.name = "Mumbi"
    dest1.desc = "City that never sleeps"
    dest1.img = "destination_1.jpg"
    dest1.price = 700
    
    dest2 = Destination()
    dest2.name = "Indonesia"
    dest2.desc = "The land of culture"
    dest2.img = "destination_2.jpg"
    dest2.price = "450"
    
    dest3 = Destination()
    dest3.name = "San Francisco"
    dest3.desc = "The Chinese Fortune Cookie was Born Here"
    dest3.img = "destination_3.jpg"
    dest3.price = 1000
    
    dest4 = Destination()
    dest4.name = "Paris"
    dest4.desc = "City of Love, Fashion, Culture"
    dest4.img = "destination_4.jpg"
    dest4.price = 800
    
    dest5 = Destination()
    dest5.name = "Baltic Sea"
    dest5.desc = "production of food and beverages, electronics and the traditional stalwarts of machine building"
    dest5.img = "destination_5.jpg"
    dest5.price = "600"
    
    dest6 = Destination()
    dest6.name = "MyKonos"
    dest6.desc = "high energy that attracts a diverse and upscale crowd who thrive on its dance-till-dawn nightlife"
    dest6.img = "destination_8.jpg"
    dest6.price = "1500"
    
    destinations = [dest1, dest2, dest3, dest4, dest5, dest6]
    
    return render(request, 'site/index.html', {'destinations' : destinations})