from django.db import models

# Create your models here.
class Shift_description(models.Model):
    main_id = models.AutoField(primary_key=True)
    shift_code = models.CharField(max_length=5)
    shift_name = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()
    def __str__(self):
        return self.shift_code

class Operation_data(models.Model):
    main_id = models.AutoField(primary_key=True)
    operation_name = models.CharField(max_length=25)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()
    def __str__(self):
        return self.operation_name

class Machine_data(models.Model):
    main_id = models.AutoField(primary_key=True)
    machine_number = models.CharField(max_length=12)
    machine_description = models.CharField(max_length=25)
    operation_id = models.ForeignKey(Operation_data, on_delete=models.CASCADE, default=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()
    def __str__(self):
        return self.machine_number

class Component_description(models.Model):
    main_id = models.AutoField(primary_key=True)
    component_type = models.CharField(max_length=25)
    component_lk_number = models.CharField(max_length=25)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()
    def __str__(self):
        return self.component_type

class Laser_production_data(models.Model):
    main_id = models.AutoField(primary_key=True)
    employee_id = models.CharField(max_length=10)
    shift_id = models.ForeignKey(Shift_description, on_delete=models.CASCADE, default=True, null=True)
    machine_id = models.ForeignKey(Machine_data, on_delete=models.CASCADE, default=True, null=True)
    component_id = models.ForeignKey(Component_description, on_delete=models.CASCADE, default=True, null=True)
    component_lot_number = models.CharField(max_length=5)
    component_quantity = models.CharField(max_length=5)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    objects = models.Manager()
