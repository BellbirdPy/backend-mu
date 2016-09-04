#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from forms import *
from establecimiento.models import Establecimiento


# Create your views here.
def home(request):
    return render(request,'index_page.html',{})

def bienvenida(request):
    return render(request,'bienvenida.html',{})

def login_view(request):
    state = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Te has logueado correctamente!"
                return redirect('/sistema')
            else:
                state = "Tu cuenta no esta activa, por favor ponte en contacto con el administrador."
        else:
            state = "Tu nombre de usuario y/o contraseña no coinciden."

    return render(request,'login_page.html',{'state':state})

@login_required(None,'login','/login/')
def logout_view(request):
    logout(request)
    return redirect("/")

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
            new_user.first_name = form.cleaned_data['nombre']
            new_user.last_name = form.cleaned_data['apellido']
            new_user.save()
            return redirect('/login/')
        else:
            return render(request,'register_page.html',{'form':form})
    else:
        form = RegistrationForm()

    return render(request,'register_page.html',{'form':form})

@login_required(None,'login','/login/')
def cuenta_view(request):
    user = request.user
    establecimientos = Establecimiento.objects.filter(Q(owner=user) | Q(miembros=user.miembros.all())).exclude(estado='B')

    return render(request,'cuenta.html',{'user':user,'establecimientos':establecimientos})

@csrf_protect
@ensure_csrf_cookie
@login_required(None, 'login', '/login/')
def index(request):
    return render(request, 'index.html')

def pricing_view(request):
    return render(request,'pricing.html')

def contact_view(request):
    return render(request,'contact.html')