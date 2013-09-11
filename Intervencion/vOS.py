from forms import *
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import ObraSocial

def listado(request):
	latest_ObraSocial_list = ObraSocial.objects.all().order_by('nombre')
	return render_to_response('obraSocial.html',{'latest_ObraSocial_list': latest_ObraSocial_list,})


def add(request):
    form = ObraSocialForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
        return redirect(listado)
    return render_to_response('obraSocial_add.html',
                             {'obraSocial_form': form},
                              context_instance=RequestContext(request))

	
