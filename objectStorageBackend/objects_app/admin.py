from django.contrib import admin
from .models import CustomUser, Object


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    filter_horizontal = ['accessed_objects']


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ['file_name', 'size', 'date_and_time', 'type', 'owner']
