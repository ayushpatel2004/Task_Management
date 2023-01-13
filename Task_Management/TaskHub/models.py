from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    contact = models.IntegerField(max_length=9999999999)
    password = models.CharField(max_length=150)

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