from django.contrib import admin

# Register your models here.

class MyModelAdmin(admin.ModelAdmin):
    class Media:   
        css = {
             'all': ('css/admin.css',)
        }