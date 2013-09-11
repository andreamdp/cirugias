from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import Contact, PhoneNo
from forms import *
from models import Medico, MedicoGrid

def inicio(request):
	return render_to_response("indice.html")
    
def view(request):
 grid = MedicoGrid(request)
 return render_to_response(
  "grid/object_list.html",
  {
   "grid": grid,
  },
  context_instance = RequestContext(request)
 )
 
def medicos(request):
	latest_medico_list = Medico.objects.all().order_by('nombre')
	return render_to_response('medicos.html',{'latest_medico_list': latest_medico_list,})

def medico_add(request):
	form = MedicoForm(request.POST or None)
	if form.is_valid():
		cmodel = form.save()
		cmodel.save()
		return redirect(medicos)
	return render_to_response('medico_add.html',{'medico_form': form}, context_instance=RequestContext(request))


def contacts(request):
    latest_contact_list = Contact.objects.all().order_by('name')
    
    return render_to_response('contacts.html',
    {'latest_contact_list': latest_contact_list,})

def contact_add(request):
    # sticks in a POST or renders empty form
    form = ContactForm(request.POST or None)
    if form.is_valid():
        cmodel = form.save()
        #This is where you might chooose to do stuff.
        #cmodel.name = 'test1'
        cmodel.save()
        return redirect(contacts)

    return render_to_response('contact_add.html',
                              {'contact_form': form},
                              context_instance=RequestContext(request))
                              
def contact_edit(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        contact = form.save()
        #this is where you might choose to do stuff.
        #contact.name = 'test'
        contact.save()
        return redirect(contacts)

    return render_to_response('contact_edit.html',
                              {'contact_form': form,
                               'contact_id': contact_id},
                              context_instance=RequestContext(request))
def medico_edit(request, medico_id):
    medico = get_object_or_404(Medico, pk=medico_id)
    form = MedicoForm(request.POST or None, instance=medico)
    if form.is_valid():
        medico = form.save()
        #this is where you might choose to do stuff.
        #contact.name = 'test'
        medico.save()
        return redirect(medicos)

    return render_to_response('medico_edit.html',
                              {'medico_form': form,
                               'medico_id': medico_id},
                              context_instance=RequestContext(request))                              

def contact_delete(request, contact_id):
    c = Contact.objects.get(pk=contact_id).delete()
    return redirect(contacts)

def medico_delete(request, medico_id):
    c = Medico.objects.get(pk=medico_id).delete()
    return redirect(medicos)


