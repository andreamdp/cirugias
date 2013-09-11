from forms import *
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import Paciente

def add(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
        return redirect(pacientes)
    
    return render_to_response('paciente_add.html',
                             {'paciente_form': form},
                              context_instance=RequestContext(request))

def pacientes(request):
	latest_paciente_list = Paciente.objects.all().order_by('nombre')
	return render_to_response('pacientes.html',{'latest_paciente_list': latest_paciente_list,})

def edit(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        paciente = form.save()
        paciente.save()
        return redirect(pacientes)

    return render_to_response('paciente_edit.html',
                              {'paciente_form': form,
                               'paciente_id': paciente_id},
                              context_instance=RequestContext(request))   
