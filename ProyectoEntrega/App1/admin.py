#está por defecto la línea de abajo
from django.contrib import admin 
#importo todo con el *, sino debería nombrarlo uno por uno
from .models import *

# Acá abajo van los 3 models
admin.site.register(Pacientes)
admin.site.register(Profesional)
admin.site.register(Turno)
