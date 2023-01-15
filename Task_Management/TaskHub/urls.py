from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/',views.signInPage,name='signInPage'),
    path('signup/',views.signUpPage,name='signUpPage'),
    path('clientLoggedIn/',views.clientLoggedIn, name='clientLoggedIn'),
    path('home/',views.home,name='home'),
    path('clientRegistered/',views.clientRegistered, name='clientRegistered'),
    path('AddGroup/',views.AddGroup, name='AddGroup'),
    path('GroupDetails/',views.GroupDetails, name='GroupDetails'),
    path('GroupDisplay/',views.GroupDisplay,name='GroupDisplay'),
    path('UserAdd/',views.UserAdd,name='UserAdd'),
    path('logout/',views.LogOut,name='LogOut'),
    path('TaskAdd/',views.TaskAdd,name='TaskAdd'),
    path('TaskAdded/',views.TaskAdded,name='TaskAdded'),
    path('TaskDone/',views.TaskDone,name='TaskDone'),
    path('TaskCompleted/',views.TaskCompleted,name='TaskCompleted'),
]