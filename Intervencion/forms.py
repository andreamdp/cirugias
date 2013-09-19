from django import forms
from models import Medico, VCC, Diagnostico, Paciente, Medico, Direccion, ObraSocial
from django.forms import ModelForm
from django.contrib.admin import widgets
from django.forms import ModelForm
from models import Contact, PhoneNo


class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        
class VCCForm(ModelForm):
    class Meta:
        model = VCC
        
    def __init__(self, *args, **kwargs):
        super(VCCForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget = widgets.AdminDateWidget()
        
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
