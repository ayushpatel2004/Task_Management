from django.urls import path
from . import views

urlpatterns = [
    path('', views.signInPage, name='signInPage'),
    path('signup/',views.signUpPage,name='signUpPage'),
    path('clientLoggedIn/',views.clientLoggedIn, name='clientLoggedIn'),
    path('clientRegistered/',views.clientRegistered, name='clientRegistered'),
    path('AddGroup/',views.AddGroup, name='AddGroup'),
    path('GroupDetails/',views.GroupDetails, name='GroupDetails'),
    path('UserAdd/',views.UserAdd, name='UserAdd'),
]