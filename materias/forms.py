# -*- coding: utf-8 -*-
from .models import *
from django import forms


class CrearMateriaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CrearMateriaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = 'Nombre'
        self.fields['nombre'].required = True
        self.fields['profesor'].label = 'Profesor'
        self.fields['profesor'].required = True

    class Meta:
        model = Materia
        fields = (
            'nombre',
            'profesor'
        )

        widgets = {
            'nombre': forms.TextInput(attrs={'required': 'true', 'max_length': '200'}),
            'profesor': forms.Select(attrs={'required': 'true'}),
        }

    def clean(self):

        cleaned_data = super(CrearMateriaForm, self).clean()
        ident = cleaned_data.get("nombre")

        try:
            if Materia.objects.filter(nombre=ident):
                self._errors['nombre'] = [
                    'Ya existe una materia con este nombre ']
        except:
            pass

