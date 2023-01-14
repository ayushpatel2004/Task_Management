from django.template import loader
from django.shortcuts import render, redirect

from django.shortcuts import render
from django.http import HttpResponse

from .models import User,Groups,Tasks

from django.contrib.auth.hashers import make_password, check_password


def landing(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({},request))

def signInPage(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({},request))

def signUpPage(request):
    template=loader.get_template('signup.html')
    return HttpResponse(template.render({},request))

def home(request):
    template=loader.get_template('home.html')
    client_username = request.session['username']
    clients=User.objects.filter(username=client_username)
    groups=clients[0].groups.all()
    context={
        'user':clients[0],
        'groups':groups
    }
    return HttpResponse(template.render(context,request))

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
    request.session['username'] = client_username
    print("Session username 1 : ", request.session.get('username'))
    return redirect('../home/')


def clientRegistered(request):
    client_username=request.POST['username']
    client_password =request.POST['password']
    client_first_name = request.POST['firstname']
    client_last_name = request.POST['lastname']
    client_contact = request.POST['contact']
    hashed_client_password=make_password(client_password)
    client_email=request.POST['email']
    client_confirm_password=request.POST['cpassword']
    template=loader.get_template('home.html')
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
    request.session['username'] = client_username
    return redirect('../home/')

def AddGroup(request):
    # print(request.POST['username'])
    username=request.session['username']
    users=User.objects.filter(username=username).values()
    template=loader.get_template('groupdetails.html')
    context={
        'username':username
        # more to be added
    }
    return HttpResponse(template.render(context,request))

def GroupDetails(request):
    username=request.session['username']
    template1=loader.get_template('userdetailsadd.html')
    users=User.objects.filter(username=username)
    groupname=request.POST['groupname']
    groupdescription=request.POST['groupd']
    group=Groups(groupname=groupname,owner=username,groupdescription=groupdescription)
    group.save()
    group.members.add(users[0])
    group.save()
    request.session['groupid'] = group.id
    # print(request.session['groupid'])
    # context={
    #     'username':username,
    #     'groupid':group.id
    # }
    return HttpResponse(template1.render({},request))


def UserAdd(request):
    groupid=request.session['groupid']
    template1=loader.get_template('userdetailsadd.html')
    template2=loader.get_template('groupinfo.html')
    print(groupid)
    if request.method=='POST' and 'add' in request.POST:
       membername=request.POST['membername']
       group=Groups.objects.get(id=groupid)
       member=User.objects.filter(username=membername)
    #    group=Groups.objects.filter(groupname=groupname)
       if(len(member.values())==0):
            message="USERNAME DOES NOT EXIST"
            context={
                "message":message, 'group': group
            }
            return render(request,'message.html',context)
       group.members.add(member[0])
       group.save()
       currentmembers=group.members.values().all()
       context={
         'members': currentmembers
       }
       return HttpResponse(template1.render(context,request))
    if request.method=='POST' and 'continue' in request.POST:   
    #    group=Groups.objects.get(groupname=groupname)
    #    context={
    #       'groupid': groupid,'username':username
    #    }
       return redirect('../GroupDisplay')


def TaskAdd(request):
    username = request.session['username']
    groupid=request.session['groupid']
    template=loader.get_template('taskadd.html')
    return HttpResponse(template.render({},request))


def TaskAdded(request):
    username = request.session['username']
    groupid=request.session['groupid']
    template1=loader.get_template('taskadd.html')
    # template2=loader.get_template('groupmainpage.html')
    if request.method=='POST' and 'add' in request.POST:
       taskname=request.POST['taskname']
       taskdescription=request.POST['taskdescription']
       points=request.POST['taskdescription']
       assignedto=request.POST['taskdescription']
       group=Groups.objects.get(id=groupid)
       group.tasknum=group.tasknum+1
       group.percentage=((group.taskcompleted)*100)/(group.tasknum)
       task=Tasks(taskname=taskname, taskdescription=taskdescription,completionstatus=0, assignedto=assignedto,points=points )
       task.save()
       group=Groups.objects.get(id=groupid)
       group.tasks.add(task)
       group.save()
       return HttpResponse(template1.render({},request))
    if request.method=='POST' and 'continue' in request.POST:
       return redirect('../GroupDisplay')


def GroupDisplay(request): 
    if request.method=='POST' and 'group_open_home' in request.POST:
        groupid=request.POST['groupid']
    else :
        groupid=request.session['groupid']
    # print("ID : ", request.session['groupid'])
    username = request.session['username']
    group=Groups.objects.get(id=groupid)
    template=loader.get_template('groupinfo.html')
    template1=loader.get_template('groupinfo.html')
        
    if(group.owner==username):
        completed=group.tasks.filter(completionstatus=1)
        pending=group.tasks.filter(completionstatus=0)
        context={
            'completed': completed ,
            'pending' : pending ,
            'groupid' : groupid
        }
        return HttpResponse(template1.render(context,request))
    
    else :
        memberslist=group.members.exclude(username=group.owner)
        memberslist.get(username=username).username="You"
        if request.method=='POST' and 'teammate_tasks' in request.POST:
            teammate=request.POST['teammate']
            members=memberslist.exclude(username=teammate)
            tasks=group.tasks.get(assignedto=teammate)
            completed=tasks.filter(completionstatus=1).all()
            pending=tasks.filter(completionstatus=0).all()
            context={
                'completed': completed ,
                'pending' : pending ,
                'members': members,
                'currentuser':teammate,
                'groupid' : groupid
            }
            return HttpResponse(template.render(context,request))

        else :
            members=memberslist.exclude(username=username)
            tasks=group.tasks.get(assignedto=username)
            completed=tasks.filter(completionstatus=1).all()
            pending=tasks.filter(completionstatus=0).all()
            context={
                'completed': completed ,
                'pending' : pending ,
                'members': members,
                'currentuser':username,
                'groupid' : groupid
            }
            return HttpResponse(template.render(context,request))

def TaskDone(request):
    taskid=request.POST['taskid']
    groupid=request.session['groupid'] 
    group=Groups.objects.get(id=groupid)
    task=Tasks.objects.get(taskid=taskid)
    task.completionstatus=1
    task.save()
    username=request.session['username'] 
    user=User.objects.get(username)
    user.score=user.score+task.points
    user.save()
    group.taskcompleted=group.taskcompleted+1
    group.percentage=((group.taskcompleted)*100)/(group.tasknum)
    group.save()
    return redirect('/GroupDisplay')

def LogOut(request):
    del request.session['username']
    return redirect('../login/')

def GroupSessionEnd(request):
    del request.session['groupid']
    return redirect('../home/')
