from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('products', views.products, name="products"),
    path('vendors', views.vendors, name="vendors"),
    path('news', views.news, name="news"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('photos', views.photos, name="photos"),

  
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)