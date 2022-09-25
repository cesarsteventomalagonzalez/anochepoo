from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from Ventas.models import Categoria,Productos,Empresa
class ClienteListView(ListView):
    template_name = "linea/list.html"
    model = Categoria
    context_object_name = 'lineas'
    paginate_by = 6
    #queryset = Cliente.objects.filter(estado=True)

    def get_queryset(self):
        query = self.request.GET.get("query")
        print(query)
        if query:
            return self.model.objects.filter(nombres__icontains=query)
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'LISTADO DE LINEAS'
        context['query'] = self.request.GET.get("query") or ""
        return context
