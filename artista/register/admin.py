from django.contrib import admin
import csv
from django.http import HttpResponse
# Register your models here.
from .models import User
from .forms import AdminUserForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('uuid','display_name', 'email', 'user_role','address','phoneNumber', 'created_at','id',)
    search_fields = ['email','display_name']
    readonly_fields=['uuid','password' ,'created_at']

    # form = AdminUserForm
    add_form = AdminUserForm
    
    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def has_add_permission(self, request):
        return True

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["password", "uuid",'created_at']
        else:
            return []
    actions = ["export_as_csv"]
    
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"
    
    pass

