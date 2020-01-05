from django.contrib import admin

# Register your models here.
from .models import Employee, Activation

admin.site.register(Employee)
admin.site.register(Activation)