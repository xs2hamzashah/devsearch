from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.profiles, name='profiles'),
    path('profile/<str:pk>', view=views.userProfile, name='user-profile'),
]
