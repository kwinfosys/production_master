from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Component_description, Shift_description, Laser_production_data, Machine_data, Operation_data
from django.contrib.messages import *
from django.urls import reverse

# Create your views here.
def show_home_page (request):
    return render(request,'home.html')

