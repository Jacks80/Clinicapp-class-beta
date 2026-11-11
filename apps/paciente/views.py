
from django.shortcuts import render, redirect
from .forms import PacienteForm
from .models import Paciente

# Create your views here.

def add_paciente(request):
    template_name = 'pacientes/add_paciente.html'
    context = ()
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('core:home')
        form = PacienteForm()
        context['form'] = form
        return render(request, template_name, context)
