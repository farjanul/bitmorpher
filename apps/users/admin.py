from django.contrib import admin

from apps.users.models import CustomUserModel


@admin.register(CustomUserModel)
class CustomUserModelAdmin(admin.ModelAdmin):
    pass
