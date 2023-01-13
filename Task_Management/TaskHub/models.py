from django.db import models


# Create your models here.
class Groups(models.Model):
    groupname=models.CharField(max_length=300)
    owner=models.CharField(max_length=300)
    groupdescrition=models.CharField(max_length=300)
    members=models.ManyToManyField(User)


class Tasks(models.Model):
    taskname=models.CharField(max_length=300)
    completionstatus=models.CharField(max_length=300)
    assignedto=models.CharField(max_length=300)
    taskdescription=models.CharField(max_length=300)
    groupname=models.ForeignKey(Groups, on_delete=models.CASCADE)