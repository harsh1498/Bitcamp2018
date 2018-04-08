from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
	#home page for all user
    path('index',views.index, name='index'),
   	#all users
    path('home',views.home,name='home'),
	#patient interface
    path('searchdoc',views.search_doc,name='searchdoc'),
    	#patient
    path('seehealthrecords',views.see_health_instance,name='health_instance'),
    	#for all users
    path('login',login, {'template_name':'home/login.html'}),
    	#all users
    path('signup',views.signup, name='signup'),
  	#patient
    path('createhealthinstance',views.create_health_instance, name='createhealthinstance'),
    	#patient
    path('createcommunicationpatient',views.create_communication_patient, name='createcommunication'),
    	#patient
    path('createappointment',views.create_appointment, name='createappointment'),
    	#patient
    path('viewchat',views.view_communication, name='viewchat'),
    	#doctor
    path('viewdocchat',views.view_doc_chat, name='view_doc_chat'),
     	#doctor
    path('createcommunicationdoctor',views.create_communication_doctor, name='commdoc'),
    	#doctor
    path('calender',views.calender, name='calender'),
	#alluser 
   path('logout',logout),
]
