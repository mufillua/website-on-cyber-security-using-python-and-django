from django.urls import path
from . import views
urlpatterns=[
    path('test',views.test),
    path('home',views.home),
    path('kali',views.kali),
    path('androidguide',views.androidguide),
    path('linuxguide',views.linuxguide),
    path('windowsguide',views.windowsguide),
    path('spam',views.spam),
    path('cyberthreats',views.cyberthreats),
    path('aws',views.aws),
    path('awssecurity',views.awssecurity),
    path('services',views.services),
    path('ser',views.ser),
    path('showcomplains',views.showcomplains),
    path('signup',views.signup),
    path('sig',views.sig),
    path('login',views.login),
    path('log_code',views.logcode),
    
]