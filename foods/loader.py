import json

with open('Restaurant.json', 'r') as f :
    Restaurants = json.load(f)
    
new_list = []

for Restaurant in Restaurants :
    new_data = {"model" : "foods.Restaurant"}
    new_data['fields'] = Restaurant
    new_list.append(new_data)
    
with open('Restaurants.json', 'w', encoding='UTF-8') as f :
    json.dump(new_list, f, ensure_ascii=False, indent=2)