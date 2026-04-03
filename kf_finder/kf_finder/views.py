
from django.shortcuts import render
from food.models import Dish,Restaurant,Feedback
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


def home(request):
    return render(request, "landing.html")

from django.db.models import Q

def dishes(request):
    q = request.GET.get("q")
    dishes = Dish.objects.all()

    if q:
        q = q.lower()
        dishes = dishes.filter(
            Q(name__icontains=q) |
            Q(category__icontains=q) |
            Q(region__icontains=q) |
            Q(taste__icontains=q)
        )

    return render(request, "dishes.html", {"dishes": dishes})

from django.db.models import Q

def dish_list(request, name=None):
    q = request.GET.get("q", "").strip()

    if name:
        # show ONE dish
        dish = Dish.objects.get(name=name)

        # Show restaurants linked through dish1, dish2, or dish3
        restaurants = Restaurant.objects.filter(
            Q(dish1=dish) | Q(dish2=dish) | Q(dish3=dish)
        )

        return render(request, "dish_detail.html", {
            "dish": dish,
            "restaurants": restaurants
        })

    # otherwise show ALL dishes + search filter
    dishes = Dish.objects.filter(
        Q(name__icontains=q) |
        Q(category__icontains=q) |
        Q(region__icontains=q) |
        Q(description__icontains=q) |
        Q(taste__icontains=q)
    )

    return render(request, "dishes.html", {"dishes": dishes})

def restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request, "restaurants.html", {"restaurants": restaurants})


def taste_search(request):
    taste = request.GET.get("taste", "")

    if taste:
        dishes = Dish.objects.filter(category__icontains=taste)
    else:
        dishes = Dish.objects.all()

    return render(request, "taste.html", {"dishes": dishes})

def feedback(request):
    dishes = Dish.objects.all()
    restaurants = Restaurant.objects.all()

    if request.method == "POST":
        dish_id = request.POST.get("dish")
        restaurant_id = request.POST.get("restaurant")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        Feedback.objects.create(
            dish_id=dish_id,
            restaurant_id=restaurant_id,
            rating=rating,
            comment=comment
        )

        return render(request, "feedback.html", {
            "success": True,
            "dishes": dishes,
            "restaurants": restaurants
        })

    return render(request, "feedback.html", {
        "dishes": dishes,
        "restaurants": restaurants
    })