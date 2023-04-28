from django.contrib import admin
from user.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

# When you define an Inline, you allow users to edit information on 
# related models directly from the edit form of the main model (in this case, User model)
class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inline = []
        return super(AuthUserAdmin, self).add_view(*args, **kwargs)
        
    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline]
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)
    #inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)
