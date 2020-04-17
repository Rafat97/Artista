from django.contrib import admin

# Register your models here.
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'email', 'user_role', 'created_at','id',)
    search_fields = ['email','display_name']
    readonly_fields=['password',]
    # form =  ClientUserForm
    # raw_id_fields = ("newspaper")
    # form = ClientUserForm
    
    pass

