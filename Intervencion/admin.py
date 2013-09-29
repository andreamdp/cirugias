# -*- encoding: utf-8 -*-
from django.contrib import admin
from forms import *
from Intervencion.models import *
admin.site.register(ObraSocial)
admin.site.register(Medico)

admin.site.register(Complicacion)
admin.site.register(TipoPreparacion)
admin.site.register(ExtensionAnatomica)
admin.site.register(Terapeutica)
admin.site.register(VCC_Indicacion)

class VccAdmin(admin.ModelAdmin):
	form = VCCForm
	list_display = ('nroEstudio', 'fecha', 'hora')
	#list_filter = ('ciudad',)
	#list_display_links = list_display
	#search_fields = list_display
	
	fieldsets = (
		('Datos del Estudio',
			{
			'fields':(('nroEstudio', 'fecha', 'hora','tiempoTotal', 'tiempoRetirada'),)
			}
		),
		('Datos del Paciente',
			{
			'fields':(('paciente', 'sexo', 'ObraSocial'),)
			}
		),
		('Diagnósticos',
			{
			'fields':(('diagnostico1', 'diagnostico2', 'diagnostico3','diagnostico4'),)
			}
		),
		('Profesionales',
			{
			'fields':(('endoscopista', 'solicitante', 'anestesista','asistente'),)
			}
		),
		('Datos',
			{
			'fields':(('complicacion', 'tipoPreparacion', 'extensionAnatomica','terapeutica'),
			('hallazgo', 'comentario', 'motivo','tacto'),
			)
			}
		),
		)
admin.site.register(VCC,VccAdmin)		


