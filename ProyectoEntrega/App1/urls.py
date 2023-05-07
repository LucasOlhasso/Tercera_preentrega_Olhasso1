from django.urls import path 
from App1 import views 

urlpatterns=[

    path('', views.inicio, name="Inicio"),
    path('Pacientes', views.Paciente, name="Pacientes"),
    path('Profesional', views.Profesional, name="Profesional"),
    path('Turnos', views.Turnos, name="Turnos"),
    path('PacientesFormulario', views.pacientesFormulario, name="PacientesFormulario"),
    path('ProfesionalFormulario', views.ProfesionalesFormulario, name="ProfesionalFormulario"),
    path('TurnosFormulario', views.turnoFormulario, name="TurnosFormulario"),
    path('busquedaPacientes', views.busquedaPacientes, name="BusquedaPacientes"),
    path('buscar/',views.buscar),
]