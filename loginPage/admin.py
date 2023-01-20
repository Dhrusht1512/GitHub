from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomAdmin(UserAdmin):
    list_display = ['username', 'user_type']


admin.site.register(CustomUser)
