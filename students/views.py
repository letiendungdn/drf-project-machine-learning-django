from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def students(request):
    students = [
        {'id': 1, 'name': 'Alice', 'age': 20},
    ]
    return HttpResponse(students)