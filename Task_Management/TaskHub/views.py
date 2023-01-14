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

# def home(request):
#     template=loader.get_template('home.html')
#     clients=User.objects.filter(username=client_username).values()
#     context={
#         'user':clients[0]
#         # more to be added
#     }
#     return HttpResponse(template.render(context,request))

def clientLoggedIn(request):
    client_username=request.POST['username']
    client_password=request.POST['password']
    # print(request.POST['password'])
    clients=User.objects.filter(username=client_username).values()
    if(len(clients)==0):
        message="USERNAME DOES NOT EXIST"
        context={
            "message":message
        }
        return render(request,'message.html',context)

    saved_hashed_password = clients[0]['password']
    # saved_role=clients[0]['role']
    
    if(check_password(client_password,saved_hashed_password)!=True):
        message="WRONG PASSWORD"
        context={
            "message":message
        }
        return render(request,'message.html',context)
    template=loader.get_template('home.html')
    context={
        'user':clients[0]
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
    client_confirm_password=request.POST['cpassword']

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
    print(request.POST['username'])
    username=request.POST['username']
    users=User.objects.filter(username=username).values()
    template=loader.get_template('groupdetails.html')
    context={
        'user':users[0]
        # more to be added
    }
    return HttpResponse(template.render(context,request))

def GroupDetails(request):
    username=request.POST['username']
    template1=loader.get_template('groupdetails.html')
    # template2=loader.get_template('groupmainpage.html')
    users=User.objects.filter(username=username).values()
    # print('shinjan')
    if request.method=='POST' and 'add_group' in request.POST:
       groupname=request.POST['groupname']
       groupdescription=request.POST['groupd']
       context={
         'user':users[0],
         'groupname': groupname,
         'groupdescription': groupdescription
       }
       group=Groups(groupname=groupname,owner=username,groupdescription=groupdescription)
       group.save()
       return HttpResponse(template1.render(context,request))
    if request.method=='POST' and 'add' in request.POST:
       groupname=request.POST['groupname']
       membername=request.POST['membername']
       member=User.objects.filter(username=membername)
       group=Groups.objects.filter(groupname=groupname)
       if(len(member.values())==0):
            message="USERNAME DOES NOT EXIST"
            context={
                "message":message
            }
            return render(request,'message.html',context)
       print(member[0])
       group[0].members.add(member[0])
       group[0].save()
       user= User.objects.filter(username=username)
       groups=user[0].groups.all()
       print(groups.values())
       return HttpResponse(template1.render({},request))
    if request.method=='POST' and 'continue' in request.POST:   
       groupname=request.POST['groupname']
       group=Groups.objects.get(groupname=groupname)
       context={
          'group': group[0],'user':users[0]
       }
       return HttpResponse(template2.render(context,request))








    
    