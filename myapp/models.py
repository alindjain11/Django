from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Restaurant(models.Model):
    name = models.TextField()
    street = models.TextField()
    number = models.TextField()
    city = models.TextField()
    zipcode = models.TextField()
    state = models.TextField()
    country = models.TextField()
    telephone = models.TextField()
    #url = models.URLField()
    #user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
class Student(models.Model):
    name=models.CharField(max_length=20)

class Dish(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.TextField('Dollars')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to='myrestaurants', default='/home/alind/Downloads/FullSizeRender.jpg')
    restaurant = models.ForeignKey(Restaurant, related_name='dishes',on_delete=models.CASCADE)


class Review(models.Model):
    RATING= ((1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five'))
    rating=models.PositiveSmallIntegerField('Rating(stars)', default=3, choices=RATING)
    comment=models.TextField()
    #user=models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)


class Employee(models.Model):
    emp_id= models.CharField(max_length=50)
    emp_name= models.CharField(max_length=50)
    competency= models.CharField(max_length=50)
    suggest= models.CharField(max_length=50)
    emp_img=models.ImageField(upload_to='Employee')
