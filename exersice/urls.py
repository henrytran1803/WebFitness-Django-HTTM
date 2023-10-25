from django.urls import path, include
from . import views
urlpatterns = [
    path('exersice/exersice/<int:page_number>/', views.exersice, name='exersice'),
    path('exercise/exercise_detail/<int:exercise_id>/<int:page_number>/', views.exercise_detail, name='exercise_detail'),
]
