from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee

def firstView(request):
    data = Employee.objects.all()
    return JsonResponse({'data': list(data.values('name', 'salary'))})