from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .forms import (
    UserCreationForm,UserChangeForm,AdminPasswordChangeForm,UserAdminCreationForm,UserAdminChangeForm
)
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)


User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserAdminChangeForm
    # add_form = UserAdminCreationForm

    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('email','password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','current_password',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ( 'date_joined','last_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name','last_name','password1', 'password2'),
        }),
    )
    readonly_fields = ('current_password',)
    
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    list_display = ('email', 'id', 'first_name', 'last_name', 'is_staff','is_superuser')
    ordering = ('id',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)


