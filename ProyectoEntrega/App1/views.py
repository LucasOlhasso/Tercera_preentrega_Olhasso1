from django.shortcuts import render
#from App1.models import Curso
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')
def Pacientes(request):
    return render(request, 'App1/Pacientes.html')
def Profesional(request):
    return render(request, 'App1/Profesional.html')
def Turnos(request):
    return render(request, 'App1/Turnos.html')
def cursoFormulario(request):
      if request.method == 'POST':
            curso =  Curso(request.post['nombre'],(request.post['curso']))
            curso.save()
            return render(request, "App1/inicio.html")
      return render(request,"App1/cursoFormulario.html")
