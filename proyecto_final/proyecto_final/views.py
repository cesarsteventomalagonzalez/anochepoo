from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *
from Ventas.models import Empresa


class Principal(TemplateView):
    template_name = 'principal.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Bienvenido al menu principal"
        context['url_anterios'] = "/Ventas/menu"
        context['nombre'] = Empresa.objects.values("nombre")
        context['contacto'] = Empresa.objects.values("contacto")
        context['correo'] = Empresa.objects.values("correo")
        return context


class Linea(TemplateView):
    template_name = 'parte/categoria.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Bienvenido a mis Lineas"

        return context
class Linealist(ListView):
    model = Linea
    template_name = 'parte/categoria.html'

class Productos(TemplateView):
    template_name = 'parte/quienessomos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Bienvenido a Prodcutos"

        return context



