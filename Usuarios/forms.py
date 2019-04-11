# -*- coding: utf-8 -*-
from .models import *
from django import forms
from django.contrib.auth.forms import *


class IniciarSesion(AuthenticationForm):
    class Meta:
        model = User

        username = forms.CharField(label="Usuario", max_length=100,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
        password = forms.CharField(label="Contraseña", max_length=100,
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class CrearUsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CrearUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Primer nombre'
        self.fields['last_name'].label = 'Primer apellido'
        self.fields['email'].label = 'Correo Electronico'
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

    class Meta:
        model = Usuario
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
        )

        widgets = {

            'last_name': forms.TextInput(attrs={'required': 'true', 'max_length': '100'}),
            'first_name': forms.TextInput(attrs={'required': 'true', 'max_length': '100'}),
            'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }

    def clean(self):

        cleaned_data = super(CrearUsuarioForm, self).clean()
        correo = cleaned_data.get("email")

        try:
            if User.objects.filter(username=correo):
                self._errors['email'] = [
                    'Ya existe un usuario con este correo electrónico']
        except:
            pass


class ModificarUsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModificarUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Primer nombre'
        self.fields['last_name'].label = 'Primer apellido'

    class Meta:
        model = Usuario

        fields = (
            'first_name',
            'last_name',
            'password',
        )


        widgets = {
            'last_name': forms.TextInput(attrs={'required': 'true', 'max_length': '100', 'readonly': 'readonly'}),
            'first_name': forms.TextInput(attrs={'required': 'true', 'max_length': '100', 'readonly': 'readonly'}),
            'password': forms.PasswordInput(),

        }
