from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.food, name='food'),
]
