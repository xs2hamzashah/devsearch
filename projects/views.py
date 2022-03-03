from django.shortcuts import redirect, render

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
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)