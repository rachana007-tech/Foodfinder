"""
URL configuration for kf_finder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('update_dish/',views.update_dish,name='update'),
    path('add_dish/',views.add_dish,name='update'),
    path('delete_dish/',views.delete_dish,name='update'),
    path('getall_dishes/',views.get_all_dishes,name='display'),

    path('update_rest/',views.update_restaurant,name='display'),
    path('add_rest/',views.add_restaurant,name='add'),
    path('delete_rest/',views.delete_restaurant,name='delete'),
    path('getall_rest/',views.get_all_restaurants,name='display'),
    path('',views.home,name='home'),
    path('dishes/',views.dishes,name='dish_list'),
    path('dish/<path:name>/',views.dish_list,name='dish_detail'),
    path('restaurants/',views.restaurants,name='restaurant_list'),
    
    path('feedback/',views.feedback,name='feedback'),

    


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)