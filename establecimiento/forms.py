#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from models import Establecimiento

class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimiento
        fields = ['nombre']

class MiembroForm(forms.Form):
    mail = forms.EmailField()



