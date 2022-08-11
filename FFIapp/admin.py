from django.contrib import admin
from FFIapp.models import UserProfile, newsPost

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(newsPost)

class MyModelAdmin(admin.ModelAdmin):
    class Media:   
        css = {
             'all': ('css/admin.css',)
        }
