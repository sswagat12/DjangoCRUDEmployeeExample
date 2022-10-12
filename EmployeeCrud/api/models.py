from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.CharField(max_length= 15, primary_key = True)
    employee_name = models.CharField(max_length=100)
    salary_per_hour = models.IntegerField()
    working_hours = models.IntegerField()
    total_salary = models.IntegerField()
