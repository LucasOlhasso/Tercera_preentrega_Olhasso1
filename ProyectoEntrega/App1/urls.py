from django.urls import path 
from App1 import views 

urlpatterns=[

    path('', views.inicio, name="Inicio"),
    path('Pacientes', views.Pacientes, name="Pacientes"),
    path('Profesional', views.Profesional, name="Profesional"),
    path('Turnos', views.Turnos, name="Turnos"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario")
]