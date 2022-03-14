from django.shortcuts import render

from .models import Profile

# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    
    return render(request, 'users/profiles.html', context)


def userProfile(requset, pk):
    profile = Profile.objects.get(pk=pk)
    topSkills = profile.skill_set.exclude(description__exact='')
    otherSkills = profile.skill_set.filter(description='')
   
    context = {'profile':profile, 'topSkills':topSkills, 'otherSkills':otherSkills}
    return render(requset, 'users/user-profile.html', context)

