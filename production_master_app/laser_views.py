from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Component_description, Shift_description, Laser_production_data, Machine_data, Operation_data
from django.contrib.messages import *
from django.urls import reverse

# Create your views here.
def show_laser_page (request):
    component_data = Component_description.objects.all()
    shift_data = Shift_description.objects.all()
    production_data = Laser_production_data.objects.all()
    machine_data = Machine_data.objects.all()
    opertion_data = Operation_data.objects.all()
    context = {'components': component_data, 'shifts': shift_data, 'products': production_data, 'operations': opertion_data, 'machines': machine_data}
    return render(request,'laser.html',context)

def add_production (request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        emp_number = request.POST.get('employee_no')
        shift_code = request.POST.get('shift_code')
        machine_code = request.POST.get('machine_number')
        component_type = request.POST.get('component_type')
        lot_number = request.POST.get('lot_number')
        quantity = request.POST.get('quantity')
        shift_code_obj = Shift_description.objects.get(main_id = shift_code)
        machine_obj = Machine_data.objects.get(main_id = machine_code)
        component_obj = Component_description.objects.get(main_id = component_type)
        production_data_object = Laser_production_data(employee_id=emp_number,shift_id=shift_code_obj,machine_id = machine_obj ,component_id=component_obj,component_lot_number=lot_number,component_quantity=quantity,created_at=datetime.datetime.now(),updated_at=datetime.datetime.now())
        production_data_object.save()
        success(request,"Production added successfully...")
        return HttpResponseRedirect(reverse('laser'))

