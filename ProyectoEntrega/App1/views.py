from django.shortcuts import render
from App1.models import Pacientes, Profesional, Turno
from django.http import HttpResponse
from App1.forms import PacientesFormulario, ProfesionalFormulario, TurnosFormulario

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def Paciente(request):
    return render(request, 'App1/Pacientes.html')
def Profesionales(request):
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

def profesionalFormulario(request):
      if request.method == "POST":
            miFormulario = ProfesionalFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  prof = Profesional(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']),
                                   informacion['mail'], informacion['profesion'])
                  prof.save()
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
                  t = Turno(int(informacion['id']),str(informacion['nombrepaciente']),str(informacion['nombreprofesional']),informacion['fechaturno'],informacion['turnovigente'])
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

def leerProfesional(request):
    profesional = Profesional.objects.all() # trae a todos los profesionales
    contexto = {"profesional": profesional}
    return render(request, "App1/leerProfesional.html",contexto)

def mostrarPacientes(request):
    pacientes = Pacientes.objects.all() # trae a todos los profesionales
    contexto = {"pacientes": pacientes}
    return render(request, "App1/mostrarPacientes.html",contexto)

def eliminarProfesional(request, profesional_nombre):
    profesional = Profesional.objects.get(nombre=profesional_nombre)
    profesional.delete()
    # vuelvo al menú
    profesional = Profesional.objects.all()  # trae todos los profesionales
    contexto = {"profesional": Profesional}
    return render(request, "App1/inicio.html", contexto)

##clases basadas en vistas para Profesional
from django.views.generic import ListView
class ProfesionalList(ListView):
    model =Profesional 
    template_name='/App1/profesional_list.html'

from django.views.generic.detail import DetailView
class ProfesionalDetalle(DetailView):
    model=Profesional 
    template_name= "App1/profesional_detalle.html"

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
class ProfesionalCreacion(CreateView):
    model=Profesional
    success_url="/App1/prosional/list"
    fields= ['nombre','apellido','mail','profesion']

from django.views.generic.edit import UpdateView
class ProfesionalUpdate(UpdateView):
    model=Profesional
    success_url= "/App1/profesional/list"
    fields=['nombre','apellido','mail','profesion']

from django.views.generic.edit import DeleteView
class ProfesionalDelete(DeleteView):
    model=Profesional
    success_url="/App1/profesional/list"

#Clases basadas en vistas para Pacientes

class PacientesList(ListView):
    model =Pacientes 
    template_name='/App1/pacientes_list.html'

class PacientesDetalle(DetailView):
    model=Pacientes
    template_name= "App1/pacientes_detalle.html"

class PacientesCreacion(CreateView):
    model=Pacientes
    success_url="/App1/pacientes/list"
    fields= ['nombre','apellido','dni']

class PacientesUpdate(UpdateView):
    model=Pacientes
    success_url= "/App1/pacientes/list"
    fields= ['nombre','apellido','dni']

class PacientesDelete(DeleteView):
    model=Pacientes
    success_url="/App1/pacientes/list"


