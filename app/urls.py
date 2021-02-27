from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('crud', views.crud, name='crud'),
    path('display', views.display, name='display'),
    path('covid', views.covid, name='covid'),
    path('delete/<int:id>', views.delete, name='delete'),

]