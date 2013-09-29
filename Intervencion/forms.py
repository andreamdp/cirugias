from django import forms
from models import Medico, VCC, Diagnostico, Paciente, Medico, Direccion, ObraSocial, Complicacion
from django.forms import ModelForm
from django.contrib.admin import widgets
from django.forms import ModelForm
from models import Contact, PhoneNo

import datetime
class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        
class VCCForm(ModelForm):
    
		

    class Meta:
        model = VCC
        
        widgets = { 'hallazgo':  forms.Textarea(attrs={'rows':2}),
        'motivo':  forms.Textarea(attrs={'rows':2}),
        'hallazgo':  forms.Textarea(attrs={'rows':2}),
        'comentario':  forms.Textarea(attrs={'rows':2}),
        'tacto':  forms.Textarea(attrs={'rows':2})
		}
    def __init__(self, *args, **kwargs):
        super(VCCForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget = widgets.AdminDateWidget()

class ComplicacionForm(ModelForm):
    class Meta:
        model = Complicacion
class PhoneNoForm(ModelForm):
    class Meta:
        model = PhoneNo
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact

class DiagnosticoForm(ModelForm):
    class Meta:
        model = Diagnostico
        
class PacienteForm(ModelForm):
    class Meta:
        model = Paciente

class DireccionForm(ModelForm):
    class Meta:
        model = Direccion

class ObraSocialForm(ModelForm):
    class Meta:
        model = ObraSocial

class DiagnosticoForm(ModelForm):
    class Meta:
        model = Diagnostico
