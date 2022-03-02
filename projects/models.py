from email.policy import default
from pyexpat import model
from django.db import models
import uuid


# Create your models here.

class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True) # null(db) blank(form)
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)

    tags = models.ManyToManyField('Tag', blank=True)

    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    # owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False) 
    body =  models.TextField(null=True, blank=True)
    value = models.CharField(max_length=255, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.project} {self.value} "


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False) 

    def __str__(self) -> str:
        return self.name