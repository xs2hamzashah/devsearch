from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),

    path('', view=views.profiles, name='profiles'),
    path('profile/<str:pk>', view=views.userProfile, name='user-profile'),
    path('account/', view=views.userAccount, name='account'),
    
    path('edit-account/', view=views.editAccount, name='edit-account'),
    
    path('create-skill/', view=views.createSkill, name='create-skill'),
    path('update-skill/<str:pk>', view=views.updateSkill, name='update-skill'),
    path('delete-skill/<str:pk>', view=views.deleteSkill, name='delete-skill'),
]
