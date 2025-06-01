from django.contrib import admin
from .models import Owner, Animal

# Register your models here.

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id','category','status','owner']
    list_filter = ['status']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone']