from django.contrib import admin
from .models import Employee, Building, Subdivision

admin.site.register(Employee)
admin.site.register(Subdivision)
admin.site.register(Building)