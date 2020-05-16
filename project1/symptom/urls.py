"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
#from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   url('basic',views.basic,name='basic'),
   url('login',views.login,name='login'),
   url('registration',views.registration,name='registration'),
   url('logout',views.logout,name='logout'),
   url('contact',views.contact1,name='contact'),
   url('covid19',views.covid,name='covid'),
   url('covidstate',views.covidstate,name='covidstate'),
   url('covidworld',views.covidworld,name='covidworld'),
   url('prevention',views.prevention,name='prevention'),
   url('treatment',views.treatment,name='treatment'),
   url('symptoms',views.symptoms,name='symptoms'),
   url('about',views.about,name='about'),
   url('indiadata',views.indiadata,name='indiadata'),
   url('bodyloc', views.bodyloc, name='bodyloc'),
   url('subbody', views.subbody, name='subbody'),
   url('bodydata', views.bodydata, name='bodydata'),
   url('result',views.result,name='result'),
   url('diagme',views.diagme,name='diagme'),
]
