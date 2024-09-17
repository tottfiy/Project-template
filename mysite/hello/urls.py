from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('secret-game', views.secret_santa, name="santa")
]