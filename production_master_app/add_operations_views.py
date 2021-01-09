from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Component_description, Shift_description, Laser_production_data, Machine_data, Operation_data
from django.contrib.messages import *
from django.urls import reverse

def show_operation_page (request):
    operation_data = Operation_data.objects.all()
    context = {'operations':operation_data}
    return render(request,'add_operations.html',context)

def add_operation (request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        operation_name = request.POST.get('operation_name')
        operation_data_object = Operation_data(operation_name=operation_name, created_at=datetime.datetime.now(),updated_at=datetime.datetime.now())
        operation_data_object.save()
        success(request,"Operation added successfully...")
        return HttpResponseRedirect(reverse('operation'))