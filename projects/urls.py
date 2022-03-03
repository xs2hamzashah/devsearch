from django.urls import path
from . import views

urlpatterns = [
    path('single-project/<str:pk>', views.project, name='project'),
    path('projects', views.projects, name='projects'),

    path('create-project', views.create_project, name='create-project'),

    path('update-project/<str:pk>/', views.update_project, name='update-project'),
]
