![django-user-model](https://user-images.githubusercontent.com/63022500/235317506-854a0f09-7ba6-4974-bff4-45e2c25fd1f2.jpg)

# Django-Complete-Studies
Complete Django Studies

### CustomUserModel:

The class "AuthUser" inherits from User default model, and it is possible to filter if the
user is active or not:

To access all users:

```
AuthUser.objects.all()
```

To filter by users:

```
AuthUser.inactive.all()
AuthUser.active.all()
```

To access if a user is active:

```
x = AuthUser.objects.get(id=3)
check_active(x)
```

<hr />

### ExtendedUserFields:

The class UserProfile has fields that are added to the default user model
and model forms are created and the user form is shown together with the user profile fields 
##### Default User fields: 
      - First name
      - Last name
##### Extended user fields:
      - Age
      - Nickname
      
<img width="393" alt="extended-form" src="https://user-images.githubusercontent.com/63022500/235264606-b57b4060-cde6-46d7-94cd-3f025bcb64d2.png">

### ExtendedUserFields2

The class NewUser inherits from AbstractUser and it allows being able to extend the User Model and create new fields. 

##### **Step by Step**:

Step 1 - Change models.py to

```
from django.db import models
from django.contrib.auth.models import AbstractUser

class NewUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=100, null=True, blank=True)
```

Step 2 - Add the following line in settings.py to

```
AUTH_USER_MODEL = 'user.NewUser'
```

Step 3 - Allows the information to display in the User Menu. In admin.py:

```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser

class CustomUserAdmin(UserAdmin):
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

admin.site.register(NewUser, CustomUserAdmin)
```
or 
```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import NewUser

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Information', {'fields': ('first_name', 'last_name', 'email', 'age', 'nickname')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(NewUser, UserAdmin)
```
The result:

<img width="695" alt="additional-fields" src="https://user-images.githubusercontent.com/63022500/235317940-d935a4ac-259b-427c-8e82-e084c1049e4e.png">


