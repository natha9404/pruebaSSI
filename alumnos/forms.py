# -*- coding: utf-8 -*-
from .models import *
from django import forms


class CrearAlumnoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CrearAlumnoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = 'Nombre'
        self.fields['nombre'].required = True
        self.fields['DNI'].label = 'DNI'
        self.fields['DNI'].required = True
        self.fields['materia'].label = 'Materias a Matricular'
        self.fields['materia'].required = True

    class Meta:
        model = Alumno
        fields = (
            'nombre',
            'DNI',
            'materia'
        )

        widgets = {
            'nombre': forms.TextInput(attrs={'required': 'true', 'max_length': '200'}),
            'DNI': forms.NumberInput(attrs={'required': 'true', 'max_length': '10'}),
            'materia': forms.SelectMultiple(attrs={'required': 'true'}),

        }

    def clean(self):

        cleaned_data = super(CrearAlumnoForm, self).clean()
        ident = cleaned_data.get("DNI")

        try:
            if Alumno.objects.filter(DNI=ident):
                self._errors['DNI'] = [
                    'Ya existe un alumno con este DNI ']
        except:
            pass

