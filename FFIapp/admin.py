from django.contrib import admin
from FFIapp.models import UserProfile

# Register your models here.

admin.site.register(UserProfile)

class MyModelAdmin(admin.ModelAdmin):
    class Media:   
        css = {
             'all': ('css/admin.css',)
        }
