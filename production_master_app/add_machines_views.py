from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Component_description, Shift_description, Laser_production_data, Machine_data, Operation_data
from django.contrib.messages import *
from django.urls import reverse

def show_machine_page (request):
    machine_data = Machine_data.objects.all()
    operation_data = Operation_data.objects.all()
    context = {'machines':machine_data, 'operations':operation_data}
    return render(request,'add_machines.html',context)

def add_machine (request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        machine_number = request.POST.get('machine_number')
        operation_id = request.POST.get('operation_id')
        operation_name_object = Operation_data.objects.get(main_id=operation_id)
        machine_description = request.POST.get('machine_description')
        machine_data_object = Machine_data(machine_number=machine_number, operation_id = operation_name_object, machine_description= machine_description, created_at=datetime.datetime.now(),updated_at=datetime.datetime.now())
        machine_data_object.save()
        success(request,"Machine added successfully...")
        return HttpResponseRedirect(reverse('machine'))