# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group

import re


alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Unicamente se aceptan caracteres alfanumericos.')
alpha = RegexValidator(r'^[a-zA-Z]*$', 'Unicamente se aceptan caracteres alfanumericos.')
numeric = RegexValidator(r'^[0-9]*$', 'Solamente valores númericos')

# Create your models here.


class Usuario(User):

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)