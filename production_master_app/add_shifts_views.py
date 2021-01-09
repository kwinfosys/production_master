from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Component_description, Shift_description, Laser_production_data, Machine_data, Operation_data
from django.contrib.messages import *
from django.urls import reverse

def show_shift_page (request):
    shift_data = Shift_description.objects.all()
    context = {'shifts': shift_data}
    return render(request,'add_shifts.html',context)

def add_shift (request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        shift_code = request.POST.get('shift_code')
        shift_name = request.POST.get('shift_name')
        shift_data_object = Shift_description(shift_code=shift_code, shift_name=shift_name,created_at=datetime.datetime.now(),updated_at=datetime.datetime.now())
        shift_data_object.save()
        success(request,"Shift added successfully...")
        return HttpResponseRedirect(reverse('shift'))
    