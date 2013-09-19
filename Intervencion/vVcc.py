from forms import *
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

def add(request):
    form = VCCForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
        return redirect(medicos)
    return render_to_response('vcc_add.html',
                             {'vcc_form': form},
                              context_instance=RequestContext(request))

	
def vcc(request):
	latest_vcc_list = VCC.objects.all().order_by('nroEstudio')
	return render_to_response('vcc.html',{'latest_vcc_list': latest_vcc_list,})

    
def edit(request, vcc_id):
    vcc = get_object_or_404(VCC, pk=vcc_id)
    form = VCCForm(request.POST or None, instance=vcc)
    if form.is_valid():
        vcc = form.save()
        #this is where you might choose to do stuff.
        #contact.name = 'test'
        vcc.save()
        return redirect(vcc)

    return render_to_response('vcc_edit.html',
                              {'vcc_form': form,
                               'vcc_id': vcc_id},
                              context_instance=RequestContext(request))                              
