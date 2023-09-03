from django import forms
from django.forms import ModelForm
from FFIapp.models import models, newsPost

class newsPostForm(ModelForm):
    class Meta:
        model = newsPost
        fields = ('title', 'message', 'author',)

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'id': 'titleBar'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'id':'messageBar'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'authortag', 'type':'hidden'}),
        }

class newCustomerForm(forms.Form):
    First_Name = forms.CharField(help_text="First Name")
    Last_Name = forms.CharField(help_text="Last Name")

class newMarinaForm(forms.Form):
    Name = forms.CharField(help_text="Marina Name", max_length=50)
    Street = forms.CharField(help_text="Street Address", max_length=50)
    City = forms.CharField(max_length=25)
    Zip = forms.IntegerField(max_value="99999")

