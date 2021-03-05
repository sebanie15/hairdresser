from django.contrib import admin

from .models import Employee, Salon

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email_address', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email_address', 'phone_number')
    ordering = ('last_name', 'first_name')
    list_filter = ('first_name', 'last_name', 'email_address', 'phone_number')


class SalonAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'open_from', 'open_to')
    search_fields = ('name', 'address', 'phone_number')
    ordering = ('name', )
    # list_filter = ('first_name', 'last_name', 'email_address', 'phone_number')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Salon, SalonAdmin)
