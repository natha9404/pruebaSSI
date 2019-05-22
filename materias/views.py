from django.views.generic import CreateView, ListView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.


class CrearMateria(CreateView):
    model = Materia
    form_class = CrearMateriaForm
    template_name = "crear_materia.html"
    success_url = reverse_lazy('listar_materias')

    def form_valid(self, form):
        return super(CrearMateria, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al registrar la materia, por favor revise los datos")
        return super(CrearMateria, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearMateria, self).get_context_data(**kwargs)
        context['modificar'] = False
        context['materias'] = True
        return context



class ListarMaterias(ListView):
    model = Materia
    template_name = "listar_materias.html"

    def get_context_data(self, **kwargs):
        context = super(ListarMaterias, self).get_context_data(**kwargs)
        context['materias'] = True
        return context
