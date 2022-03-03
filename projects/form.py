from dataclasses import fields
from django.forms import ModelForm
from .models import Project

from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image',  'description', 'demo_link', 'source_link','tags']

        widgets = {
        'tags': forms.CheckboxSelectMultiple(),

        }
    
    def __init__(self,  *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs.update({'class': 'input'})
        # This is used add custom css class to django forms
        for name,field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})