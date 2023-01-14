from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    contact = models.IntegerField(max_length=9999999999)
    password = models.CharField(max_length=150)
    score=models.IntegerField(default=0)

# Create your models here

class Tasks(models.Model):
    taskname=models.CharField(max_length=300)
    completionstatus=models.CharField(max_length=300)
    assignedto=models.CharField(max_length=300)
    taskdescription=models.CharField(max_length=300)
    points=models.IntegerField(max_length=100, default=0)
    # groupname=models.ForeignKey(Groups, on_delete=models.CASCADE)

class Groups(models.Model):
    groupname=models.CharField(max_length=300)
    owner=models.CharField(max_length=300)
    groupdescription=models.CharField(max_length=300)
    members=models.ManyToManyField(User,related_name='groups')
    tasks=models.ManyToManyField(Tasks,related_name='groups')
    tasknum=models.IntegerField(max_length=1000000,default=0)
    taskcompleted=models.IntegerField(max_length=1000000, default=0)
    percentage=models.FloatField(max_length=100, default=0)