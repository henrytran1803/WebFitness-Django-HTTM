from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.food, name='food'),
    path('track/', views.tracking, name='track'),
    path('eat_track/<int:track_id>/', views.eat_track_detail, name='eat_track_detail'),
    path('track/detail/', views.detail, name='detail'),
]
