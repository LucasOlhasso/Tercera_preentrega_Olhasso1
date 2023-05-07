from django.shortcuts import render
from App1.models import Pacientes, Profesional, Turno
from django.http import HttpResponse
from App1.forms import PacientesFormulario, ProfesionalFormulario, TurnosFormulario

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def Paciente(request):
    return render(request, 'App1/Pacientes.html')
def Profesional(request):
    return render(request, 'App1/Profesional.html')
def Turnos(request):
    return render(request, 'App1/Turnos.html')

def pacientesFormulario(request):
      if request.method == "POST":
            miFormulario = PacientesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  pacientes = Pacientes(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),int(informacion['dni']))
                  pacientes.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = PacientesFormulario()
 
      return render(request, "App1/PacientesFormulario.html", {"miFormulario": miFormulario})

def ProfesionalesFormulario(request):
      if request.method == "POST":
            miFormulario = ProfesionalFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  profe = Profesional(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['email'], informacion['profesion'])
                  profe.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = ProfesionalFormulario()
 
      return render(request, "App1/ProfesionalFormulario.html", {"miFormulario": miFormulario})


def turnoFormulario(request):
      if request.method == "POST":
            miFormulario = TurnosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  t = Turno(int(informacion['id']),str(informacion['nombrepaciente']),str(informacion['nombreprofesional']),informacion['fecha'], informacion['turnovigente'])
                  t.save()
                  return render(request, "App1/inicio.html")
      else:
            miFormulario = TurnosFormulario()
 
      return render(request, "App1/TurnosFormulario.html", {"miFormulario": miFormulario})

def busquedaPacientes(request):
     return render(request,'App1/busquedaPacientes.html')

def buscar(request):
     if request.GET['pacientes']:
          pacientes = request.GET['pacientes']
          Pacientes= Pacientes.objects.filter(pacientes__icontains=pacientes)

          return render(request,'App1/resultadosBusqueda.html', {"pacientes":pacientes, "comisiones": Pacientes })
     else:
          respuesta= "No ingresaste datos o los mismos no se encuentran en nuestra base"

     return HttpResponse(respuesta)
