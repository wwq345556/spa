from django.contrib import admin
from .models import Flora

# Register your models here.
class FloraAdmin(admin.ModelAdmin):
    list_display = ['flora_name']
    list_per_page = 5

admin.site.register(Flora,FloraAdmin)