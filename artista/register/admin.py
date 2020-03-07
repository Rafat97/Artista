from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'email', 'user_role', 'created_at')
    pass

