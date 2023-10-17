from django.urls import path, include

from WebSite import settings
from . import views
urlpatterns = [
    path('', views.login_f, name='login'),
    path("logout/", views.logout, name="logout"),
]
