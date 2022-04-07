from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Hero)
admin.site.register(models.Villain)
admin.site.register(models.Archenemy)