from django import views
# from .models import Restaurant
from django.shortcuts import render

new_list = []

f = open("/Users/jeon-eunbae/Documents/food/Restaurants.csv", 'r', encoding="UTF-8")
lines = f.readlines()
for line in lines :
    new_list.append(line.replace("\n", "").split(","))
f.close()

datas = new_list[1:]

def test(request) :
    return render(request, 'pages/main.html')
