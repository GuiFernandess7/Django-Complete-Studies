from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Extends default User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    nickname = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
# Occurs after save of an User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created: bool, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)