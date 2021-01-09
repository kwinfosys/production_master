"""production_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from production_master_app import views, laser_views, add_components_views, add_machines_views, add_operations_views, add_shifts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_home_page, name='home'),
    path('laser/', laser_views.show_laser_page, name='laser'),
    path('component/', add_components_views.show_component_page, name='component'),
    path('shift/', add_shifts_views.show_shift_page, name='shift'),
    path('operation/', add_operations_views.show_operation_page, name='operation'),
    path('machine/', add_machines_views.show_machine_page, name='machine'),
    path('add_production', laser_views.add_production, name='production'),
    path('add_shift', add_shifts_views.add_shift, name= 'addshift'),
    path('add_component', add_components_views.add_component, name= 'addcomponent'),
    path('update_component', add_components_views.update_component, name= 'updatecomponent'),
    path('delete_component', add_components_views.delete_component, name= 'deletecomponent'),
    path('add_operation', add_operations_views.add_operation, name= 'addoperation'),
    path('add_machine', add_machines_views.add_machine, name= 'addmachine'),
    path('edit_component/<str:main_id>', add_components_views.edit_component,name="edit_component"),
    path('delete_show_component/<str:main_id>', add_components_views.delete_show_component,name="delete_show_component"),
]