from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Servicio

# Create your views here.
def holaMundo(request):
    return HttpResponse("Hola Mundo ADSO")

def inicio(request):
    return render(request, 'inicio.html')

#def lista_servicios(request):
    servicios_list = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios_list})

def detalle(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)
    return render(request, 'detalle.html', {'servicio': servicio})

def lista_servicios(request):
    tipo_servicio = request.GET.get('tipo_servicio')
    if tipo_servicio:
        servicios = Servicio.objects.filter(tipo_servicio=tipo_servicio)
    else:
        servicios = Servicio.objects.all()
    return render(request, 'servicios.html', {'servicios': servicios})