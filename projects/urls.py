from django.urls import path
from . import views

urlpatterns = [
    path('projects/<str:pk>', views.projects, name='project')
]
