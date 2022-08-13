from tkinter import HIDDEN
from django import forms
from django.forms import ModelForm
from FFIapp.models import models, newsPost

class newsPostForm(ModelForm):
    class Meta:
        model = newsPost
        fields = ('title', 'message', 'author',)

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'authortag', 'type':'hidden'}),
        }