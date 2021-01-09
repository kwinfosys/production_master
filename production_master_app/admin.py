from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Shift_description)
admin.site.register(Component_description)
admin.site.register(Laser_production_data)
admin.site.register(Operation_data)
admin.site.register(Machine_data)