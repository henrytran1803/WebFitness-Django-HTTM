from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.blog, name='blog'),
    path('blog_details/', views.blog_details, name='blog_details'),
]
