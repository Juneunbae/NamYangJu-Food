from django import views
from .models import Restaurant, check
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

def map_list(request) :
    res = Restaurant.objects.all()
    context = {
        'res' : res,
    }
    return render(request, 'pages/list.html', context)