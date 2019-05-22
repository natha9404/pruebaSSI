# -*- coding: utf-8 -*-
from .models import *
from django import forms


class CrearProfesorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CrearProfesorForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = 'Nombre'
        self.fields['nombre'].required = True
        self.fields['cedula'].label = 'Cédula'
        self.fields['cedula'].required = True

    class Meta:
        model = Profesor
        fields = (
            'nombre',
            'cedula'
        )

        widgets = {
            'nombre': forms.TextInput(attrs={'required': 'true', 'max_length': '200'}),
            'cedula': forms.NumberInput(attrs={'required': 'true', 'max_length': '12'}),
        }

    def clean(self):

        cleaned_data = super(CrearProfesorForm, self).clean()
        ident = cleaned_data.get("cedula")

        try:
            if Profesor.objects.filter(cedula=ident):
                self._errors['cedula'] = [
                    'Ya existe un profesor con esta cédula ']
        except:
            pass

