from django.contrib import admin
from .models import CustomOrder,Cal
from django.db.models import Q

# Register your models here.

@admin.register(CustomOrder)
class CustomOrderAdmin(admin.ModelAdmin):
    list_display = [ "title","name", "email", "phone"]
    def has_add_permission(self, request):
        return False

@admin.register(Cal)
class CalAdmin(admin.ModelAdmin):
    list_display = [ "length","width","area"]
    
