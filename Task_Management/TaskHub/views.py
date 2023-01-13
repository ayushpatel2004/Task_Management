from django.template import loader
from django.shortcuts import render, redirect

from django.shortcuts import render
from django.http import HttpResponse

from .models import User,Groups,Tasks

from django.contrib.auth.hashers import make_password, check_password

# hashed_pwd = make_password("plain_text")
# check_password("plain_text",hashed_pwd)


def signInPage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def signUpPage(request):
    template=loader.get_template('signup.html')
    return HttpResponse(template.render({},request))

def home(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render({},request))

def clientLoggedIn(request):
    client_username=request.POST['username']
    client_password=request.POST['password']
    clients=User.objects.filter(username=client_username).values()
    if(len(clients)==0):
        message="USERNAME DOES NOT EXIST"
        context={
            "message":message
        }
        return render(request,'message.html',context)

    saved_hashed_password = clients[0]['password']
    saved_role=clients[0]['role']
    
    if(saved_role!=0):
        message="NOT A VALID CLIENT"
        context={
            "message":message
        }
        return render(request,'message.html',context)
    if(check_password(client_password,saved_hashed_password)!=True):
        message="WRONG PASSWORD"
        context={
            "message":message
        }
        return render(request,'message.html',context)
    template=loader.get_template('chome.html')
    context={
        'client':clients[0]
        # more to be added
    }
    return HttpResponse(template.render(context,request))


def clientRegistered(request):
    client_username=request.POST['username']
    client_password =request.POST['password']
    client_first_name = request.POST['firstname']
    client_last_name = request.POST['lastname']
    client_contact = request.POST['contact']
    hashed_client_password=make_password(client_password)
    client_email=request.POST['email']
    client_confirm_password=request.POST['confirm_password']

    for x in User.objects.all().values():
        if(x['username']==client_username):
            message="USERNAME TAKEN"
            context={
                "message":message
            }
            return render(request,'message.html',context)

    if(client_confirm_password!=client_password):
        message="PASSWORDS DO NOT MATCH"
        context={
            "message":message
        }
        return render(request,'message.html',context)
    user=User(username=client_username,password=hashed_client_password,email=client_email,firstname= client_first_name,lastname=client_last_name,contact=client_contact)
    user.save()
    return redirect('home')

def AddGroup(request):
    username=request.POST['username']
    clients=User.objects.filter(username=username).values()
    template=loader.get_template('groupdetails.html')
    context={
        'client':clients[0]
        # more to be added
    }
    return HttpResponse(template.render(context,request))

def GroupDetails(request):
    username=request.POST['username']
    template1=loader.get_template('groupdetails.html')
    template2=loader.get_template('groupmainpage.html')
    clients=User.objects.filter(username=username).values()
    if request.method=='POST' and 'add_group' in request.POST:
       groupname=request.POST['groupname']
       groupdescription=request.POST['groupd']
       group=Groups(groupname=groupname,owner=username,groupdescription=groupdescription )
       group.save()
    if request.method=='POST' and 'add' in request.POST:
       groupname=request.POST['groupname']
       membername=request.POST['membername']
       member=User.objects.get(username=membername)
       group=Groups.objects.get(groupname=groupname)
       if(len(member)==0):
        message="USERNAME DOES NOT EXIST"
        context={
            "message":message
        }
        return render(request,'message.html',context)
       group[0].User.add(member[0])
       return HttpResponse(template1.render({},request))
    if request.method=='POST' and 'continue' in request.POST:   
       groupname=request.POST['groupname']
       group=Groups.objects.get(groupname=groupname)
       context={
          'group': group[0],'client':clients[0]
       }
       return HttpResponse(template2.render(context,request))








    
    