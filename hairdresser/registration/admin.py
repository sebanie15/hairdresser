from django.contrib import admin

from .models import Salon

# Register your models here.


class SalonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'open_from', 'open_to')
    search_fields = ('name', 'address', 'phone_number')
    ordering = ('name', )
    # list_filter = ('first_name', 'last_name', 'email_address', 'phone_number')


admin.site.register(Salon, SalonAdmin)
