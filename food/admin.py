from django.contrib import admin

# Register your models here.
from .models import DetailEatTrack, EatTrack, Nutritions, Products


admin.site.register(EatTrack)
admin.site.register(Nutritions)
admin.site.register(Products)
admin.site.register(DetailEatTrack)