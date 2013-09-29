from forms import *
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import Complicacion
def complicacion(request):
	latest_vcc_list = Complicacion.objects.all()
	return render_to_response('change_listComplica.html',{'latest_vcc_list': latest_vcc_list,})

def add(request):
    form = ComplicacionForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
    #    return redirect(pacientes)
    return render_to_response('complicacion_add.html',
                             {'complicacion_form': form},
                              context_instance=RequestContext(request))
