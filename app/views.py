from django.shortcuts import render, HttpResponseRedirect
from .forms import student_form, cv_form
from .models import student, cv
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

def delete(request, id):
    if request.method == 'POST':
        data = student.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/display')
    


def covid(request):
    response = requests.get(
        "https://api.covid19api.com/summary")
    data = response.json()
    return render(request, 'covid.html', {'countries': data['Countries'], 'global':data['Global']})



def cvbuilder(request):
    if request.method == 'POST':
        cvv = cv_form(request.POST)
        if cvv.is_valid():
            cvv.save()
        cvv = cv_form()
    else:
        cvv = cv_form()
    return render(request, 'cvbuilder.html', {'cvv': cvv})

def cvdisplay(request):
    ccvv = cv.objects.all()
    return render(request, 'cvdisplay.html', {'ccvv': ccvv})