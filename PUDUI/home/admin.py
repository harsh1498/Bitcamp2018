from django.contrib import admin
from .models import health_attr, communication, health_instance, patient, doctor, insurance,doctor_appointment,prescription
# Register your models here.

admin.site.register(health_attr)
admin.site.register(communication)
admin.site.register(health_instance)
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(insurance)
admin.site.register(doctor_appointment)
admin.site.register(prescription)
