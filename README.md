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

