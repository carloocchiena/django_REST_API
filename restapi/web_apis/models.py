from django.db import models

# Create your models here.
class Hero(models.Model):
    real_name = models.CharField(max_length=50)
    hero_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Real Name: {self.real_name}, Hero Name: {self.hero_name}"