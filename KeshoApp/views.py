from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'keshoApp/index.html')

def home(request):
    return render(request, 'keshoApp/home.html')

def about(request):
    return render(request, 'keshoApp/about.html')

# def babe(request):
#     return render(request, 'keshoApp/babe.html')  

def jumper(request):
    return render(request, 'keshoApp/jumper.html')

#Trying to add a babe form
def AddBabe(request):
    # addedbabe = Babe.objects.get(id=pk)
    getbabeform = AddBabeForm()
    return render(request, 'keshoApp/babe.html', {'getbabeform': getbabeform,})
    # babesform = AddBabe(request.POST)
    # if request.method == 'POST':
    #     if babesform.is_valid():
    #         newbabe = babesform.save(commit = False)
    #         newbabe.save()
    # return render(request, 'keshoApp/babe.html', {'babesform': babesform,})
    

