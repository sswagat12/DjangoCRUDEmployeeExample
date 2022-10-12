from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.

@api_view(['GET'])
def employees_crud(request):
    emp_urls = {
        'all': '/',
        'add': '/create',
        'update': '/update/pk',
        'delete': '/delete/pk'
    }
    return Response(emp_urls)

@api_view(['POST'])
def add_employee(request):
    employee = EmployeeSerializer(data = request.data)

    if Employee.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Data duplicacy detected, please check existing records')
    if employee.is_valid():
        employee.save()
        return Response(employee.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_all_employees(request):  # sourcery skip: use-named-expression
    if request.query_params:
        employee = Employee.objects.filter(**request.query_param.dict())
    else:
        employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    if employee:
        data = EmployeeSerializer(employee)
        return Response(serializer.data)
    else:
        return Response(status = status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    data = EmployeeSerializer(instance=employee, data = request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return Response(status=status.HTTP_202_ACCEPTED)



