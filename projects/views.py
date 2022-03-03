from django.shortcuts import redirect, render

from projects.form import ProjectForm
from .models import Project

# Create your views here.



def projects(request):
    ProjectList = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': ProjectList})


def project(request, pk):
    ProjectList = Project.objects.all()
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



def update_project(request, pk): 
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')


    context = {'object':project}
    return render(request, 'projects/delete_template.html', context)