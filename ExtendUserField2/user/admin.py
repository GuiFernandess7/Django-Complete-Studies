from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser

""" class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Additional Info",
            {
                'fields': (
                    'age', 
                    'nickname',
                )
            }
        )
    )

admin.site.register(NewUser, CustomUserAdmin) """

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Information', {'fields': ('first_name', 'last_name', 'email', 'age', 'nickname')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(NewUser, UserAdmin)