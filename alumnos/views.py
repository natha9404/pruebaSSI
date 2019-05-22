from django.views.generic import CreateView, ListView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages



class CrearAlumno(CreateView):
    model = Alumno
    form_class = CrearAlumnoForm
    template_name = "crear_alumno.html"
    success_url = reverse_lazy('listar_alumnos')

    def form_valid(self, form):
        alumno = form.instance
        alumno.nombre = alumno.nombre
        alumno.DNI = alumno.DNI
        self.object = form.save()

        return super(CrearAlumno, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al registrar el alumno, por favor revise los datos")
        return super(CrearAlumno, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearAlumno, self).get_context_data(**kwargs)
        context['modificar'] = False
        context['alumnos'] = True
        return context


class ListarAlumnos(ListView):
    model = Alumno
    template_name = "listar_alumnos.html"

    def get_context_data(self, **kwargs):
        context = super(ListarAlumnos, self).get_context_data(**kwargs)
        context['alumnos'] = True
        return context