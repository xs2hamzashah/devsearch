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
]
