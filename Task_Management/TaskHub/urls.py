from django.urls import path
from . import views

urlpatterns = [
    path('', views.signInPage, name='signInPage'),
    path('signup/',views.signUpPage,name='signUpPage'),
    path('home/',views.home,name='home')
]