from django.contrib import admin


from .models import Salon, Service


# Register your models here.


class SalonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'open_from', 'open_to')
    search_fields = ('name', 'address', 'phone_number')
    ordering = ('name', )
    # list_filter = ('first_name', 'last_name', 'email_address', 'phone_number')
    fields = ('name', 'address', 'phone_number', 'open_from', 'open_to', )


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_length', 'price')
    search_fields = ('name', )
    ordering = ('name', )
    # list_filter = ('first_name', 'last_name', 'email_address', 'phone_number')
    fields = ('name', 'service_length', 'price')


admin.site.register(Salon, SalonAdmin)
# admin.site.register(User)

admin.site.register(Service, ServiceAdmin)
