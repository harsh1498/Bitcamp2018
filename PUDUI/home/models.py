from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

DATA_RELEASE_CHOICES = ((25,'25%'),(50,'50%'),(75,'75%'),(100,'100%'))

# Key value pair of the health issuse name and descriptionindex

class health_attr(models.Model):
    key = models.CharField(default='key',null=False,blank=False,max_length=50)
    value = models.CharField(default='value',null=False,blank=False,max_length=200)

    def __str__(self):
        return self.key

class insurance(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE,null=False,default=0,blank=False)
     def __str__(self):
         return str(self.user)

class doctor(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE,null=False,default=0,blank=False)
     doctor_type = models.CharField(max_length=50,default='general',null=True)
     zip_code = models.IntegerField(null=True)

     def __str__(self):
         return str(self.user)

class patient(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE,null=False,default=0,blank=False)
     doctors = models.ManyToManyField(doctor)
     insurances = models.ManyToManyField(insurance)
     data_release = models.IntegerField(choices=DATA_RELEASE_CHOICES,default=75)

     def __str__(self):
         return str(self.user)

class health_instance(models.Model):
     common_name = models.CharField(max_length=20,default="default",null=False,blank=False)
     health_attr = models.ManyToManyField(health_attr)
     description = models.CharField(max_length=300,default="default")
     timestamp = models.DateTimeField(auto_now=True)
     patient = models.ForeignKey(patient,null=False,default=0,blank=False,on_delete=models.CASCADE)
     doctor = models.ForeignKey(doctor,null=False,default=0,blank=False,on_delete=models.CASCADE)
     insurance = models.ForeignKey(insurance,null=False,default=0,blank=False,on_delete=models.CASCADE)

     def __str__(self):
         return str(self.common_name)

class prescription(models.Model):
    dosage = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    health_instance = models.ForeignKey(health_instance,null=False,default=0,blank=False,on_delete=models.CASCADE)

class doctor_appointment(models.Model):
     patient = models.ForeignKey(patient,null=False,default=0,blank=False,on_delete=models.CASCADE)
     doctor = models.ForeignKey(doctor,null=False,default=0,blank=False,on_delete=models.CASCADE)
     health_instance = models.ManyToManyField(health_instance,default=0,blank=False)
     timestamp = models.DateTimeField(auto_now=True)
     appointment_time = models.DateTimeField(default='12/12/2020 14:00')

     def __str__(self):
         return str(self.appointment_time) + ' : ' + str(self.patient) + ' : ' + str(self.doctor)


class communication(models.Model):
    patient = models.ForeignKey(patient,null=False,default=0,blank=False,on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctor,null=False,default=0,blank=False,on_delete=models.CASCADE)
    health_instance = models.ForeignKey(health_instance,null=False,default=0,blank=False,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_patient = models.BooleanField(default=False)
    message = models.CharField(default='message',null=False,blank=False,max_length=1500)

    def __str__(self):
        return self.message
