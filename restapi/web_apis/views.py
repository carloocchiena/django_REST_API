from django.shortcuts import render
from rest_framework import viewsets

from . import models, serializers

# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = models.Hero.objects.all().order_by('hero_name')
    serializer_class = serializers.HeroSerializer
    