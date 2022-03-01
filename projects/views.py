from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def projects(request, pk):
    names = ['hamza', 'rehan', 'adil', 'hamid']
    return render(request, 'projects/projects.html', {'pk':pk, 'names': names})
