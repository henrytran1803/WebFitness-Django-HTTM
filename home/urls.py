from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('<str:username>/<int:islog>/', views.index, name='index_with_params'),
    path('user/', views.user, name='user'),
    path('<str:username>/<int:islog>/user/', views.user, name='user'),
]
