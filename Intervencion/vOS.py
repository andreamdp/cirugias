from forms import *
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

def add(request):
    form = ObraSocialForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
        return redirect(medicos)
    return render_to_response('obraSocial_add.html',
                             {'obraSocial_form': form},
                              context_instance=RequestContext(request))

	
def vcc(request):
	latest_obraSocial_list = obraSocial.objects.all().order_by('nombre')
	return render_to_response('obraSocial.html',{'latest_obraSocial_list': latest_obraSocial_list,})
