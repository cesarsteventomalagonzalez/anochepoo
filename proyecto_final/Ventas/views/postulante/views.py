from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView

from Ventas.views.postulante.forms import PostulanteForm
from Ventas.models import Categoria,Productos,Empresa,Postulante


class PostulanteCreateViews(CreateView):
    model = Postulante
    template_name = "postulante/form.html"
    form_class = PostulanteForm
    success_url = reverse_lazy('Ventas:postulante')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'TRABAJA CON NOSOTROS'
        context['action'] = 'add'
        return context

class Inicio(TemplateView):
    model = Empresa
    template_name = "principal.html"
    success_url = reverse_lazy('/')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Inicio'
        context['url_anterior'] = '/'
        context['nombre'] = Empresa.objects.values("nombre")
        context['contacto'] = Empresa.objects.values("contacto")
        context['correo'] = Empresa.objects.values("correo")
        return context