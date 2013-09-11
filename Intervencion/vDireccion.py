from forms import *
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import Direccion

def add(request):
    form = DireccionForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
        return redirect(listado)
    return render_to_response('direccion_add.html',
                             {'direccion_form': form},
                              context_instance=RequestContext(request))

def listado(request):
	latest_direccion_list = Direccion.objects.all().order_by('calle')
	return render_to_response('direcciones.html',{'latest_direccion_list': latest_direccion_list,})

def eliminar(request, direccion_id):
    c = Direccion.objects.get(pk=direccion_id).delete()
    return redirect(listado)
