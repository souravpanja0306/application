from django import forms
from .models import student, cv

class student_form(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'

class cv_form(forms.ModelForm):
    class Meta:
        model = cv
        fields = '__all__'