from django.shortcuts import render
from .models import Project

# Create your views here.


ProjectList = Project.objects.all()

def projects(request):
    return render(request, 'projects/projects.html', {'projects': ProjectList})


def project(request, pk):
    for project in ProjectList:
        if str(project.id) == pk:
            return render(request, 'projects/single-project.html', {'project': project, 'pk':pk})
    
    return render(request, 'projects/single-project.html', {'pk':pk})


