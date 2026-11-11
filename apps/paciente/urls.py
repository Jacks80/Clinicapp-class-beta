from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = {
    path('add_p', views.add_paciente, name ='add_paciente'),
}