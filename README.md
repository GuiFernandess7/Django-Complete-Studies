# Django-Complete-Studies
Complete Django Studies

### CustomUserModel:

The class "AuthUser" inherites from User default model, and it is possible to filter if the
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

