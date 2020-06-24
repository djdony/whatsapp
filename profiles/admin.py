from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserAdmin(UserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'custom_group']
    list_filter = ['groups', 'is_staff', 'is_superuser', 'is_active']

    def custom_group(self, obj):
        """
        get group, separate by comma, and display empty string if user has no group
        """
        return ','.join([g.name for g in obj.groups.all()]) if obj.groups.count() else ''


admin.site.unregister(User)
admin.site.register(User, UserAdmin)