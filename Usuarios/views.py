from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages



class CrearUsuario(CreateView):
    model = Usuario
    form_class = CrearUsuarioForm
    template_name = "crear_usuario.html"
    success_url = reverse_lazy('listar_usuarios')

    def form_valid(self, form):
        usuario = form.instance
        usuario.username = usuario.email
        usuario.is_active = True
        self.object = form.save()

        return super(CrearUsuario, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al registrar el usuario, por favor revise los datos")
        return super(CrearUsuario, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(CrearUsuario, self).get_context_data(**kwargs)
        context['modificar'] = False
        context['usuarios'] = True
        return context


class EditarUsuario(UpdateView):
    model = Usuario
    template_name = "crear_usuario.html"
    success_url = reverse_lazy('listar_usuarios')
    form_class = ModificarUsuarioForm

    success_message = "El usuario fue modificado exitosamente"

    def form_valid(self, form):
        usuario = form.instance
        contra = usuario.password
        usuario.set_password(contra)
        self.object = form.save()

        return super(EditarUsuario, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
        )

    def get_context_data(self, **kwargs):
        context = super(EditarUsuario, self).get_context_data(**kwargs)
        context['modificar'] = True
        context['usuarios'] = True
        return context



class ListarUsuarios(ListView):
    model = Usuario
    template_name = "listar_usuarios.html"

    def get_context_data(self, **kwargs):
        context = super(ListarUsuarios, self).get_context_data(**kwargs)
        context['usuarios'] = True
        return context