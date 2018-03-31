from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('index',views.index, name='home'),
    path('login',login, {'template_name':'home/login.html'}),
    path('logout',logout),
]

