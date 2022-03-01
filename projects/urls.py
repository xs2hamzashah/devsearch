from django.urls import path
from . import views

urlpatterns = [
    path('single-project/<str:pk>', views.project, name='project'),
    path('projects', views.projects, name='projects')
]
