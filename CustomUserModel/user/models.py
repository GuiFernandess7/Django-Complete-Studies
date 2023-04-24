from django.db import models
from django.contrib.auth.models import User

class UserManager(models.Manager):
    def get_queryset(self):
        # Return only inactive users of the fixture settings file of users
        return super(UserManager, self).get_queryset().filter(is_active=False)

class OnlyActiveUsers(models.Manager):
    def get_queryset(self):
        # Return only active users of the fixture settings file of users
        return super(OnlyActiveUsers, self).get_queryset().filter(is_active=True)

class AuthUser(User):

    # AuthUser.inactive.all()
    inactive = UserManager()
    active = OnlyActiveUsers()

    class Meta:
        proxy = True
        ordering = ('first_name',)
    
    @classmethod
    def count_all(cls):
        return cls.objects.filter(is_active=True).count()
    
    def check_active(self):
        if self.is_active == True:
            return "You are Active"
        else:
            return "You are Not Active"

    def __str__(self):
        return self.first_name

