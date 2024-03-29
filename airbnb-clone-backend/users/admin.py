from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            'Profile',
            {
                'fields': (
                    'avatar', 
                    'username', 
                    'password',
                    'name', 
                    'email', 
                    'is_host',
                    'gender',
                    'language',
                    'currency',
                ),
                'classes': ('wide',),
            }
        ),
        (
            'Permissions',
            {
                'fields':('is_active', 'is_staff', 'is_superuser', 'groups'),
                'classes': ()
            }
        )
    )