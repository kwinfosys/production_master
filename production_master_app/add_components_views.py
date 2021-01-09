from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import Component_description, Shift_description, Laser_production_data, Machine_data, Operation_data
from django.contrib.messages import *
from django.urls import reverse

def show_component_page (request):
    component_data = Component_description.objects.all()
    context = {'components': component_data}
    return render(request,'add_components.html',context)

def add_component (request):
    if request.method != 'POST':
        return HttpResponse('Method not allowed')
    else:
        component_type = request.POST.get('component_type')
        lk_number = request.POST.get('lk_number')
        shift_data_object = Component_description(component_type=component_type, component_lk_number=lk_number,created_at=datetime.datetime.now(),updated_at=datetime.datetime.now())
        shift_data_object.save()
        success(request,"Component added successfully...")
        return HttpResponseRedirect(reverse('component'))

def edit_component (request, main_id):
    component_data = Component_description.objects.get(main_id = main_id)
    context = {'new_components' : component_data, 'component_id' : main_id}
    print(component_data)
    return render(request,"edit_components.html",context)

def update_component (request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        print("Update Component Executed")
        main_id = request.POST.get('component_id')
        component_type = request.POST.get('component_type')
        lk_number = request.POST.get('lk_number')
        try:
            updated_component=Component_description.objects.get(main_id=main_id)
            updated_component.component_type = component_type
            updated_component.component_lk_number = lk_number
            updated_component.created_at = datetime.datetime.now()
            updated_component.updated_at = datetime.datetime.now()
            updated_component.save()
            success(request,"Successfully Updated Component")
            return HttpResponseRedirect(reverse("component"))
        except:
            error(request,"Failed to Update Component")
            return HttpResponseRedirect("/")
            
def delete_show_component (request, main_id):
    component_data = Component_description.objects.get(main_id = main_id)
    context = {'new_components' : component_data, 'component_id' : main_id}
    print(component_data)
    return render(request,"delete_components.html",context)

def delete_component (request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        print("Update Component Executed")
        main_id = request.POST.get('component_id')
        component_type = request.POST.get('component_type')
        lk_number = request.POST.get('lk_number')
        try:
            print("Delete Component Executed")
            print(main_id, component_type, lk_number)
            data_to_be_deleted = Component_description.objects.get(main_id=main_id)
            data_to_be_deleted.delete()
            success(request,"Successfully Deleted Component")
            return HttpResponseRedirect(reverse("component"))
        except:
            error(request,"Failed to Delete Component")
            return HttpResponseRedirect(reverse("component"))