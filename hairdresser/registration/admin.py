from django.contrib import admin
from .models import Employee


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'phone_number', 'is_employed', 'user')
    search_fields = ('first_name', 'last_name', 'email_address', 'phone_number', 'user')


admin.site.register(Employee, EmployeeAdmin)
