from django import views
from .models import Restaurant
from django.shortcuts import render

def map(request) :
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants
    }
    return render(request, 'pages/main.html', context)

def map2(request) :
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants
    }
    return render(request, 'pages/sub.html', context)
