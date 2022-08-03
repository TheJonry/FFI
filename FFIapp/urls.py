from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('products', views.products, name="products"),
    path('vendors', views.vendors, name="vendors"),

  
]