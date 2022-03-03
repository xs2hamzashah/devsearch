from django.shortcuts import render

from projects.form import ProjectForm
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


def create_project(request):
    form = ProjectForm
    context = {'form': form}
    return render(request, "projects/project_form.html", context)