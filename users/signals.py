from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, *args, **kwargs):
    if created:
        user = instance 
        profile = Profile.objects.create(
            user = user, 
            username =user.username,
            email = user.email,
            name = user.first_name,
        )

def deleteUser(sender, instance, **kwargs):
    user = instance.user 
    user.delete()

post_save.connect(createProfile, sender=User)
post_save.connect(deleteUser, sender=Profile)
