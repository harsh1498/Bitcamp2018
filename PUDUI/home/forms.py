from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import health_instance, communication, doctor_appointment


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,required=True)
    last_name = forms.CharField(max_length=30,required=True)
    email = forms.EmailField(max_length=254,required=True)
    choices = ((1,'Doctor'),(2,'Patient'),(3,'Insurance'))
    user_type = forms.ChoiceField(choices=choices)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2','user_type')

class CreateHealthInstanceForm(ModelForm):
    class Meta:
        model = health_instance
        fields = ['common_name','health_attr','description','patient','doctor','insurance']

class CreateCommunicationPatientForm(ModelForm):
    class Meta:
        model = communication
        fields = ['message','health_instance']

class CreateAppointment(ModelForm):
    class Meta:
        model = doctor_appointment
        fields = ['health_instance','doctor','patient','appointment_time']
