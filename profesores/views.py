from django.views.generic import CreateView, ListView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages



class CrearProfesor(CreateView):
    model = Profesor
    form_class = CrearProfesorForm
    template_name = "crear_profesor.html"
    success_url = reverse_lazy('listar_profesors')

    def form_valid(self, form):
        profesor = form.instance
        profesor.nombre = profesor.nombre
        profesor.cedula = profesor.cedula
        self.object = form.save()

        return super(CrearProfesor, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al registrar el profesor, por favor revise los datos")
        return super(CrearProfesor, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearProfesor, self).get_context_data(**kwargs)
        context['modificar'] = False
        context['profesores'] = True
        return context


class ListarProfesors(ListView):
    model = Profesor
    template_name = "listar_profesores.html"

    def get_context_data(self, **kwargs):
        context = super(ListarProfesors, self).get_context_data(**kwargs)
        context['alumnos'] = True
        return context