
from django.shortcuts import render
from food.models import Dish,Restaurant
from django.http import JsonResponse

def update_dish(request):
    name_value = request.GET.get('name')
    category_value = request.GET.get('category')
    region_value = request.GET.get('region')
    desc_value = request.GET.get('description')

    dish = Dish.objects.get(name=name_value)

    dish.category = category_value
    dish.region = region_value
    dish.description = desc_value

    dish.save()

    return JsonResponse({
        'message': 'Dish Updated',
        'updated': {
            "name": dish.name,
            "category": dish.category,
            "region": dish.region,
            "description": dish.description
        }
    })
def add_dish(request):
    name_value = request.GET.get('name')
    category_value = request.GET.get('category')
    region_value = request.GET.get('region')
    desc_value = request.GET.get('description')

    dish = Dish.objects.create(
        name=name_value,
        category=category_value,
        region=region_value,
        description=desc_value
    )

    return JsonResponse({
        'message': 'Dish Inserted',
        'inserted': {
            "name": dish.name,
            "category": dish.category,
            "region": dish.region,
            "description": dish.description
        }
    })
def delete_dish(request):
    name_value = request.GET.get('name')

    dish = Dish.objects.get(name=name_value)
    dish.delete()

    return JsonResponse({
        'message': 'Dish Deleted',
        'deleted_name': name_value
    })
def get_all_dishes(request):
    dishes = Dish.objects.all().values()
    return JsonResponse(list(dishes), safe=False)
 
def update_restaurant(request):
    name_value = request.GET.get('name')
    city_value = request.GET.get('city')
    address_value = request.GET.get('address')
    dish_value = request.GET.get('dish')
    rating_value = request.GET.get('rating')

    restaurant = Restaurant.objects.get(name=name_value)

    restaurant.city = city_value
    restaurant.address = address_value
    restaurant.rating = rating_value

    # update dish using dish name
    dish_obj = Dish.objects.get(name=dish_value)
    restaurant.dish = dish_obj

    restaurant.save()

    return JsonResponse({
        'message': 'Restaurant Updated',
        'updated': {
            "name": restaurant.name,
            "city": restaurant.city,
            "address": restaurant.address,
            "dish": restaurant.dish.name,
            "rating": restaurant.rating
        }
    })

def add_restaurant(request):
    name_value = request.GET.get('name')
    city_value = request.GET.get('city')
    address_value = request.GET.get('address')
    dish_value = request.GET.get('dish')   # dish name
    rating_value = request.GET.get('rating')

    # find dish using dish name
    dish_obj = Dish.objects.get(name=dish_value)

    restaurant = Restaurant.objects.create(
        name=name_value,
        city=city_value,
        address=address_value,
        dish=dish_obj,
        rating=rating_value
    )

    return JsonResponse({
        'message': 'Restaurant Inserted',
        'inserted': {
            "name": restaurant.name,
            "city": restaurant.city,
            "address": restaurant.address,
            "dish": restaurant.dish.name,
            "rating": restaurant.rating
        }
    })
def delete_restaurant(request):
    name_value = request.GET.get('name')

    restaurant = Restaurant.objects.get(name=name_value)
    restaurant.delete()

    return JsonResponse({
        'message': 'Restaurant Deleted',
        'deleted_name': name_value
    })
def get_all_restaurants(request):
    restaurants = Restaurant.objects.all().values()
    return JsonResponse(list(restaurants), safe=False)