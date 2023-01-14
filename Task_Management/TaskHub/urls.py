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
]