from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# @receiver(post_save,sender=Profile)
def createProfile(sender, instance, created , **kwargs):
    # sender - which model send this 
    # instanced - on which instance it is triggered!
    # created - if new instance is created then it is set to True otherwise False
    if created:
        user = instance 
        profile = Profile.objects.create(user=user, username=user.username,email=user.email, name=f"{user.first_name} {user.last_name}")
    

def updateUser(sender, instance, created , **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        
        user.first_name = profile.name or ''
        user.username = profile.username or ''
        user.email = profile.email or ''
        user.save()



def deleteUser(sender, instance, **kwargs):
    user= instance.user
    user.delete()
    print('Deleting user...')


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)