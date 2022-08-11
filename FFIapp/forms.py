from socket import fromshare
from django import forms
from django.forms import ModelForm
from FFIapp.models import models, newsPost

class newsPostForm(ModelForm):
    class Meta:
        model = newsPost
        fields = ['title', 'message']

form = newsPostForm()