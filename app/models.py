from django.db import models

# Create your models here.


class student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class cv(models.Model):
    name =models.CharField(max_length=70)
    about = models.CharField(max_length=300)
    job_title = models.CharField(max_length=40)
    company_name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=300)
    education_qualification = models.CharField(max_length=70)
    skills = models.CharField(max_length=200)

    def __str__(self):
        return self.name