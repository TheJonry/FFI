from django.contrib import admin
from FFIapp.models import UserProfile, newsPost, Services, Customers, Marinas, Boats, Employees, Appointments

# Register your models here.

#admin.site.register(UserProfile)
#admin.site.register(newsPost)
admin.site.register(Services)
admin.site.register(Customers)
admin.site.register(Marinas)
admin.site.register(Boats)
admin.site.register(Employees)
admin.site.register(Appointments)


class MyModelAdmin(admin.ModelAdmin):
    class Media:   
        css = {
             'all': ('css/admin.css',)
        }
