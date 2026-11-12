from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
   path('add/', views.add_paciente, name ='add_paciente'),
]