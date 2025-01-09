from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Dessert', 'Dessert'),
        ('Main Course', 'Main Course'),
        ('Breakfast', 'Breakfast'),
        ('Vegetarian', 'Vegetarian'),
        ('Drinks', 'Drinks'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()  # Could also be a many-to-many field if you create an ingredient model
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    prep_time = models.IntegerField()  # In minutes
    cook_time = models.IntegerField()  # In minutes
    servings = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title