from django.conf.urls.defaults import patterns, include, url
from Intervencion import views
from django.conf import settings
from Intervencion import vVcc, vDiagnostico, vPaciente, vDireccion, vOS,vComplicacion
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Cirugia.views.home', name='home'),
    url(r'^$', views.inicio),
    url(r'^s$', views.view),
    url(r'^contacts/$', views.contacts),  
    url(r'^contact_add/$', views.contact_add),
    url(r'^contact_delete/(?P<contact_id>\d+)/$',views.contact_delete),
    url(r'^contact_edit/(?P<contact_id>\d+)/$',views.contact_edit),
    url(r'^medico_edit/(?P<medico_id>\d+)/$',views.medico_edit),
    url(r'medicos/$', views.medicos),
	url(r'^medico_add/$', views.medico_add),
    url(r'^medico_delete/(?P<medico_id>\d+)/$',views.medico_delete),
    url(r'^vcc_add/$', vVcc.add),
    url(r'^vcc_edit/(?P<vcc_id>\d+)/$', vVcc.edit),
    url(r'^vcc_delete/(?P<vcc_id>\d+)/$',vVcc.edit),
    url(r'^vcc/$', vVcc.vcc),
    url(r'^diagnostico_add/$', vDiagnostico.add),
	url(r'diagnosticos/$', vDiagnostico.diagnosticos),
    url(r'^diagnostico_edit/(?P<diagnostico_id>\d+)/$', vDiagnostico.edit),
    url(r'^paciente_add/$', vPaciente.add),
    url(r'^paciente_edit/(?P<paciente_id>\d+)/$', vPaciente.edit),
    url(r'^paciente_delete/(?P<paciente_id>\d+)/$',vPaciente.delete),
    url(r'pacientes/$', vPaciente.pacientes),
    url(r'^direccion_add/$', vDireccion.add),
    url(r'direcciones/$', vDireccion.listado),
    url(r'^direccion_delete/(?P<direccion_id>\d+)/$',vDireccion.eliminar),
    url(r'^obraSocial/$', vOS.listado),
    url(r'^obraSocial_add/$', vOS.add),
    url(r'^complicacion_add/$', vComplicacion.add),
	#url(r'^/Intervencion/vcc_indicacion/$', vComplicacion.complicacion),
    url('', include(admin.site.urls)),
)
urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), 
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)
