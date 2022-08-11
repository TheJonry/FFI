import re
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from FFIapp.models import newsPost

# Create your views here.
def home(request):
    return render(request, 'home.html', )


def products(request):
    return render(request, 'productMenu.html', {})

def vendors(request):
    return render(request, 'vendorMenu.html', {})

#def news(request):
#    return render(request, 'news.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def photos(request):
    return render(request, 'photos.html', {})

class newsPostView(ListView):
    model = newsPost
    template_name = "news.html"