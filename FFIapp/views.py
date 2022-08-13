import re
from django.shortcuts import render, redirect
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

def list_and_create(request):
    form = newsPostForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        form.user = request.session['user']
        form.save()
        return redirect('news/')
    
    return render(request, 'makeNews.html', )

def contact(request):
    return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})

def photos(request):
    return render(request, 'photos.html', {})

class newsPostCreateView(CreateView):
    model = newsPost
    template_name = "makeNews.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(newsPostCreateView, self).get_context_data(**kwargs)
        return context

class newsPostView(ListView):
    model = newsPost
    template_name = "news.html"
    ordering = ['-created_at']
    form_class = newsPostForm()

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-created_at')
        return ordering
    



class newsPostAddView(FormView):
    template_name = "makeNews.html"
    form_class = newsPostForm
    model = newsPost

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return redirect('news')

