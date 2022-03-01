from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
project_list = [
    {
        'id':1, 
        'title': 'E-commerce', 
        'description': 'Will soon I will build e-commerce application'
    },
    {
        'id':2, 
        'title': 'PortFolio', 
        'description': 'Within a month or two, my portfolio will be ready'
    },
    {
        'id':3, 
        'title': 'Lab-Project', 
        'description': 'Soon that prject will also be ready'
    }
]

def projects(request):
    return render(request, 'projects/projects.html', {'projects': project_list})


def project(request, pk):
    for project in project_list:
        if str(project['id']) == pk:
            return render(request, 'projects/single-project.html', {'project': project, 'pk':pk})
    
    return render(request, 'projects/project.html', {'pk':pk})


