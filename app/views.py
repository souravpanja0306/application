from django.shortcuts import render
from .forms import student_form
from .models import student
import requests

# Create your views here.

def index(request):
    return render(request, 'index.html')


def crud(request):
    if request.method == 'POST':
        stu = student_form(request.POST)
        if stu.is_valid():
            stu.save()
        stu = student_form()
    else:
        stu = student_form()
    return render(request, "crud.html", {'stu': stu})


def display(request):
    dis = student.objects.all()
    return render(request, "display.html", {'dis': dis})

# def delete(request, pk):
#     dele =


def covid(request):
    response = requests.get(
        "https://api.covid19api.com/summary")
    data = response.json()
    return render(request, 'covid.html', {'countries': data['Countries'], 'global':data['Global']})
