from django.urls import path
from App1 import views

urlpatterns=[

    path('', views.inicio, name="Inicio"),
    path('Pacientes', views.Paciente, name="Pacientes"),
    path('Profesional', views.Profesionales, name="Profesional"),
    path('Turnos', views.Turnos, name="Turnos"),
    path('PacientesFormulario', views.pacientesFormulario, name="PacientesFormulario"),
    path('ProfesionalFormulario', views.profesionalFormulario, name="ProfesionalFormulario"),
    path('TurnosFormulario', views.turnoFormulario, name="TurnosFormulario"),
    path('busquedaPacientes', views.busquedaPacientes, name="BusquedaPacientes"),
    path('buscar/',views.buscar),
    path('leerProfesional', views.leerProfesional, name='LeerProfesional'),
    path('mostrarPacientes', views.mostrarPacientes, name='MostrarPacienes'),
    path('eliminarProfesional/<profesional_nombre>/', views.eliminarProfesional, name="EliminarProfesional"),
    path('profesional/list',views.ProfesionalList.as_view(),name='List'),
        path(r'^(?P<pk>\d+)$', views.ProfesionalDetalle.as_view(),name='Detail'),
        path(r'^nuevo$', views.ProfesionalCreacion.as_view(),name='New'),
        path(r'^editar/(?P<pk>\d+)$',views.ProfesionalUpdate.as_view(),name='Edit'),
        path(r'^borrar/(?P<pk>\d+)$',views.ProfesionalDelete.as_view(),name='Delete'),
    path('pacientes/list',views.PacientesList.as_view(),name='List'),
        path(r'^(?P<pk>\d+)$', views.PacientesDetalle.as_view(),name='Detail'),
        path(r'^nuevo$', views.PacientesCreacion.as_view(),name='New'),
        path(r'^editar/(?P<pk>\d+)$',views.PacientesUpdate.as_view(),name='Edit'),
        path(r'^borrar/(?P<pk>\d+)$',views.PacientesDelete.as_view(),name='Delete')
]