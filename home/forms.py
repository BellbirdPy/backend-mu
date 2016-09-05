#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(required=True)
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    password1 = forms.CharField(max_length=100,required=True)
    password2 = forms.CharField(max_length=100,required=True)

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if username and email and password1 and password2:

            if username.islower():
                print "ok"
            else:
                msg = "El nombre de usuario debe estar en minúsculas."
                self.add_error('username', msg)

            if (' ' in username) == True:
                msg = "El nombre de usuario no debe contener espacios."
                self.add_error('username', msg)


            try:
                user = User.objects.get(email=email)
            except:
                user = None



            if user != None:
                msg = "Este email ya se ha utilizado."
                self.add_error('email', msg)

            try:
                user = User.objects.get(username=username)
            except:
                user = None

            if user != None:
                msg = "Este nombre ya se ha utilizado."
                self.add_error('username', msg)

            if password1 != password2:
                msg = "Las contraseñas no coinciden."
                self.add_error('password1', msg)
                self.add_error('password2', msg)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,required=True)
    email = forms.CharField(max_length=100,required=True)
    phone = forms.CharField(max_length=100,required=True)
    subject = forms.CharField(max_length=100,required=False)
    plan = forms.CharField(max_length=30,required=False)
    message = forms.CharField(max_length=1024,required=True)
