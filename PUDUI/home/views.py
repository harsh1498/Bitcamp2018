from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, CreateHealthInstanceForm, CreateCommunicationPatientForm, CreateAppointment
from .models import doctor, patient, insurance, health_instance, prescription, communication
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home/home.html')

def view_communication(request):
    conversations = communication.objects.filter(patient = patient.objects.get(user=request.user))
    return render(request,'home/allchats.html',{'conversations':conversations})

@login_required
def index(request):
    context = {'obj':'IDK', 'type':'IDK'}
    context['user'] = request.user
    pat = patient.objects.filter(user=request.user)
    ins = insurance.objects.filter(user=request.user)
    doc = doctor.objects.filter(user=request.user)
    if len(pat) == 1:
        context['obj'] = patient.objects.get(user=request.user)
        context['prescriptions'] = []
        for i in health_instance.objects.filter(patient=context['obj']):
            if prescription.objects.filter(health_instance=i):
                 for j in prescription.objects.filter(health_instance=i):
                    if  j.is_active:
                        context['prescriptions'].append(j)
        context['type'] = 'patient'
        return render(request, 'home/index.html',context)
    elif len(doc) == 1:
        context['obj'] = doctor.objects.get(user=request.user)
        context['type'] = 'doctor'
        return render(request, 'home/index.html',context)
    elif len(ins) == 1:
        context['obj'] = insurance.objects.get(user=request.user)
        context['type'] = 'insurance'
        return render(request, 'home/index.html',context)
    return render(request, 'home/index.html',context)

def create_communication_patient(request):
    if request.method == 'POST':
        form = CreateCommunicationPatientForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.patient = patient.objects.get(user=request.user)
            comm.doctor = comm.health_instance.doctor
            comm.is_patient = True
            comm.save()
            return redirect(index)
    else:
        form = CreateCommunicationPatientForm()

    return render(request, 'home/createhealthinstance.html', {'form':form})

def create_appointment(request):
    if request.method == 'POST':
        form = CreateAppointment(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = CreateAppointment()

    return render(request, 'home/createhealthinstance.html', {'form':form})

def search_doc(request):
    if request.method == 'POST':
        doc_type = request.POST.get('doc_type')
        context = {}
        context['doctors'] = doctor.objects.filter(doctor_type__contains=doc_type)
        return render(request,'home/searchresults.html',context=context)

    else:
        return render(request,'home/searchdoc.html')

def see_health_instance(request):
    context = {}
    pat = patient.objects.filter(user=request.user)
    if len(pat) == 1:
        context['obj'] = patient.objects.get(user=request.user)
        context['type'] = 'patient'
        context['health_instance'] = health_instance.objects.filter(patient=context['obj'])
        return render(request, 'home/healthrecords.html',context)


def create_health_instance(request):
    if request.method == 'POST':
        form = CreateHealthInstanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = CreateHealthInstanceForm()

    return render(request, 'home/createhealthinstance.html', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user_type = int(form.cleaned_data.get('user_type'))
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)

            if user_type == 1:
                doc = doctor()
                doc.user = user
                doc.save()
            elif user_type == 2:
                pat = patient()
                pat.user = user
                pat.save()
            else:
                ins = insurance()
                ins.user = user
                ins.save()
            login(request, user)
            return redirect(index)
    else:
        form = SignUpForm()

    return render(request, 'home/signup.html', {'form':form})
