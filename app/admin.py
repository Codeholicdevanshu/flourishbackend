from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Country)
class AdminCountry(admin.ModelAdmin):
    list_display=['id','date_id','generation','value']




