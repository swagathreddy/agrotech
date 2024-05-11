from django.db import models

from django.utils import timezone
class Farm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    farm_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    type_of_soil = models.CharField(max_length=100)
    type_of_crop = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.farm_name

# models.py

from django.db import models

class Farmer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.username

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title