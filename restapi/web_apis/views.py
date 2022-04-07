from django.shortcuts import render
from rest_framework import viewsets

from . import models, serializers

# Create your views here.

class HeroViewSet(viewsets.ModelViewSet):
    queryset = models.Hero.objects.all().order_by('hero_name')
    serializer_class = serializers.HeroSerializer

class VillainViewSet(viewsets.ModelViewSet):
    queryset = models.Villain.objects.all().order_by('villain_name')
    serializer_class = serializers.VillainsSerializer
    
class ArchenemyViewSet(viewsets.ModelViewSet):
    queryset = models.Archenemy.objects.all().order_by('hero')
    serializer_class = serializers.ArchenemySerializer
    