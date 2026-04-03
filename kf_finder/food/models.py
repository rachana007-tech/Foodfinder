

from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)   
    region = models.CharField(max_length=100)     
    description = models.CharField(max_length=200)
    taste = models.CharField(max_length=50,default="spicy")
    image_url=models.URLField(max_length=500,null= True,blank=True)
   

    def _str_(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    dish1 = models.ForeignKey(Dish, on_delete=models.CASCADE,null=True,blank=True,related_name="primary_dish") 
    dish2 = models.ForeignKey(Dish, on_delete=models.CASCADE,null=True,blank=True,related_name="secondary_dish")  
    dish3 = models.ForeignKey(Dish, on_delete=models.CASCADE,null=True,blank=True,related_name="third_dish")  
    rating = models.FloatField(default=4.0)
    image_url=models.URLField(max_length=500,null=True,blank=True)
    latitude=models.FloatField(null=True,blank=True)
    longitude=models.FloatField(null=True,blank=True)

    def _str_(self):
        return self.name

class Feedback(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    comment = models.TextField()

    def _str_(self):
        return f"{self.dish.name} - {self.restaurant.name}"    
