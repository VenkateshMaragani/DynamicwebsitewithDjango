from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import models


# Create your views here.

def first(request):
    return render(request,'FP_App/home.html')

def second(request):
    return render(request,'FP_App/about.html')

def thired(request):
    return render(request,'FP_App/contact.html')

def fourth(request):
    return render(request,'FP_App/gallery.html')

def fivth(request):
    return render(request,'FP_App/users.html')


def sixth(request):
    return render(request,'FP_App/services.html')


def contact_form(request):
    print("######"*5)
    form = forms.First_form() 
    print("@@@@"*5)
    if request.method=="POST":
        print(" $$$$$$*"*5)
        form = forms.First_form(request.POST)
        if form.is_valid():
            print('Form is valid')
            print('Name ', form.cleaned_data['name'])
            print('Email ',form.cleaned_data['email'])
            print('Phone No ',form.cleaned_data['phone'])

    return render(request,'FP_App/contact.html',{'form': form})

def contact(request):
    print("######"*5)
    form1 = forms.Secondform()
    if request.method=="POST":
        form = forms.Secondform(request.POST)
        if form.is_valid():
            form.save()
        return users(request)
    return render (request,'FP_App/contact.html',{'form1': form1})


def users(request):
    users=models.Contact.objects.all()

    return render(request,'FP_App/users.html',{'users': users})









