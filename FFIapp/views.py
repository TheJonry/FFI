import re
from django.shortcuts import render, redirect, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, FormView, CreateView
from FFIapp.models import *
from FFIapp.forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html', )


def products(request):
    return render(request, 'productMenu.html', {})

def vendors(request):
    return render(request, 'vendorMenu.html', {})

def news(request):
    posts = newsPost.objects.all().order_by('-created_at')
    form = newsPostForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            form = newsPostForm()
    context={
        'posts' : posts,
        'form' : form,
    }
    
    return render(request, 'news.html', context)

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def photos(request):
    return render(request, 'photos.html', {})



