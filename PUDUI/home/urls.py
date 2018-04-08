from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('index',views.index, name='index'),
    path('home',views.home,name='home'),
    path('searchdoc',views.search_doc,name='searchdoc'),
    path('seehealthrecords',views.see_health_instance,name='health_instance'),
    path('login',login, {'template_name':'home/login.html'}),
    path('signup',views.signup, name='signup'),
    path('createhealthinstance',views.create_health_instance, name='createhealthinstance'),
    path('createcommunicationpatient',views.create_communication_patient, name='createcommunication'),
    path('createappointment',views.create_appointment, name='createappointment'),
    path('viewchat',views.view_communication, name='viewchat'),
    path('viewdocchat',views.view_doc_chat, name='view_doc_chat'),
    path('createcommunicationdoctor',views.create_communication_doctor, name='commdoc'),
    path('calender',views.calender, name='calender'),
    path('logout',logout),
]
