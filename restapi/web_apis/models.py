from django.db import models

# Create your models here.
class Hero(models.Model):
    real_name = models.CharField(max_length=50)
    hero_name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Real Name: {self.real_name}, Hero Name: {self.hero_name}"
    
class Villain(models.Model):
    villain_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.villain_name
    
class Archenemy(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
    villain = models.ForeignKey(Villain, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Hero {self.hero.hero_name} hates {self.villain.villain_name}"
    