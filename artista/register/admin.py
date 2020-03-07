from django.contrib import admin

# Register your models here.
from .models import *
from .forms import ClientUserForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'email', 'user_role', 'created_at')
    search_fields = ['email','display_name']
    form = ClientUserForm
    # raw_id_fields = ("newspaper")
    # form = ClientUserForm
    
    pass

