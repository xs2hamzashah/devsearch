from django.contrib.auth.models import User

from devsearch.settings import EMAIL_HOST_USER
from .models import Profile
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.core.mail import send_mail
from django.conf import settings

# @receiver(post_save,sender=Profile)
def createProfile(sender, instance, created , **kwargs):
    # sender - which model send this 
    # instanced - on which instance it is triggered!
    # created - if new instance is created then it is set to True otherwise False
    if created:
        user = instance 
        profile = Profile.objects.create(user=user, username=user.username,email=user.email, name=f"{user.first_name} {user.last_name}")

        subject = 'Welcome to DevSearch'
        message = 'We are glad you are here!'
        
        send_mail(
            subject,
            message, 
            settings.EMAIL_HOST_USER,
            [profile.email], 
            fail_silently=False
        )
    

def updateUser(sender, instance, created , **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        
        user.first_name = profile.name or ''
        user.username = profile.username or ''
        user.email = profile.email or ''
        user.save()



def deleteUser(sender, instance, **kwargs):
    try:
        user= instance.user
        user.delete()
        print('Deleting user...')
    except:
        pass


post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)