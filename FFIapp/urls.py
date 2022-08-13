from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from FFIapp.views import *


urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('products', views.products, name="products"),
    path('vendors', views.vendors, name="vendors"),
    path('news/', views.newsPostView.as_view(), name="news"),
#    path('makeNews', views.list_and_create, name="makeNews"),
    path('makeNews', views.newsPostAddView.as_view(), name='makeNews'),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('photos', views.photos, name="photos"),

  
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]