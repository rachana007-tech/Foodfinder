

from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)   
    region = models.CharField(max_length=100)     
    description = models.CharField(max_length=200)
   

    def _str_(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)  
    rating = models.FloatField(default=4.0)

    def _str_(self):
        return self.name
