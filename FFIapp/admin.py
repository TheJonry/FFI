from django.contrib import admin
from FFIapp.models import UserProfile, newsPost, Region, Service, Customer, Marina, Boat, Employee, Appointment

# Register your models here.

#admin.site.register(UserProfile)
#admin.site.register(newsPost)
admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(Marina)
admin.site.register(Boat)
admin.site.register(Employee)
admin.site.register(Appointment)
admin.site.register(Region)


class MyModelAdmin(admin.ModelAdmin):
    class Media:   
        css = {
             'all': ('css/admin.css',)
        }
