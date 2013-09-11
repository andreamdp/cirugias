from forms import *
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

def add(request):
    form = DiagnosticoForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
        return redirect(diagnosticos)
    return render_to_response('diagnostico_add.html',
                             {'diagnostico_form': form},
                              context_instance=RequestContext(request))

def diagnosticos(request):
	latest_diagnostico_list = Diagnostico.objects.all().order_by('nombre')
	return render_to_response('diagnosticos.html',{'latest_diagnostico_list': latest_diagnostico_list,})

def edit(request, diagnostico_id):
    diagnostico = get_object_or_404(Diagnostico, pk=diagnostico_id)
    form = DiagnosticoForm(request.POST or None, instance=diagnostico)
    if form.is_valid():
        diagnostico = form.save()
        diagnostico.save()
        return redirect(diagnosticos)

    return render_to_response('diagnostico_edit.html',
                              {'diagnostico_form': form,
                               'diagnostico_id': diagnostico_id},
                              context_instance=RequestContext(request))   
