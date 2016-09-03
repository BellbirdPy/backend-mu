#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, json
from lib2to3.pgen2 import parse

from django.contrib.auth.decorators import login_required
from django.core import signing
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets, filters
from rest_framework.views import Response
from serializers import *
from models import *
from django.db.models import Q
from forms import *
import datetime
try:
    from django.contrib.sites.shortcuts import get_current_site
except ImportError:
    from django.contrib.sites.models import get_current_site


# Create your views here.
class DepartamentoViewSet(viewsets.ModelViewSet):
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()


class EstablecimientoViewSet(viewsets.ModelViewSet):
    serializer_class = EstablecimientoSerializer

    def get_queryset(self):
        """
            This view should return a list of all the purchases
            for the currently authenticated user.
            """
        #borrar esto en produccion

        if self.request.user.is_authenticated():
            return Establecimiento.objects.filter(Q(owner=self.request.user) | Q(miembros=self.request.user),estado='A')
        else:
            return Establecimiento.objects.all()

@login_required(None,'login','/login/')
def add_view(request):
    form = EstablecimientoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_establecimiento = Establecimiento()
            new_establecimiento.nombre = form.cleaned_data['nombre']
            new_establecimiento.owner = request.user
            new_establecimiento.fecha_expiracion = date.today() +datetime.timedelta(days=5)
            new_establecimiento.save()
            return redirect('/establecimiento/detail/'+str(new_establecimiento.id)+'/')
        else:
            return render(request, 'edit_establecimiento.html', {'form': form})

    return render(request,'edit_establecimiento.html',{'form':form})

@login_required(None,'login','/login/')
def detail_view(request,pk):
    establecimiento = get_object_or_404(Establecimiento, id=pk)  # or whatever is needed to get the object
    if not establecimiento.user_can_manage_me(request.user):
        return redirect('/cuenta/')
    else:
        return render(request,'detail_establecimiento.html',{'e':establecimiento})

@login_required(None,'login','/login/')
def delete_view(request,pk):
    establecimiento = get_object_or_404(Establecimiento, id=pk)  # or whatever is needed to get the object
    if not establecimiento.user_can_manage_me(request.user) or establecimiento.estado == "B":
        return redirect('/cuenta/')
    else:
        if request.method == "POST":
            if request.POST['post'] == "yes":
                establecimiento.estado = "B"
                establecimiento.save()
                return redirect('/cuenta/')
        return render(request,'delete_establecimiento.html',{'e':establecimiento})

@login_required(None,'login','/login/')
def delete_miembro_view(request,pk,pk2):
    establecimiento = get_object_or_404(Establecimiento, id=pk)  # or whatever is needed to get the object
    miembro = get_object_or_404(User,id=pk2)
    if not establecimiento.user_can_manage_me(request.user) or establecimiento.estado == "B":
        return redirect('/cuenta/')
    else:
        if request.method == "POST":
            if request.POST['post'] == "yes":
                establecimiento.miembros.remove(miembro)
                establecimiento.save()
                return redirect('/establecimiento/detail/'+str(establecimiento.id)+'/')
        return render(request,'delete_miembro.html',{'e':establecimiento,'m':miembro})

@login_required(None,'login','/login/')
def add_miembro_view(request,pk):
    establecimiento = get_object_or_404(Establecimiento, id=pk)  # or whatever is needed to get the object
    if not establecimiento.user_can_manage_me(request.user) or establecimiento.estado == "B":
        return redirect('/cuenta/')
    else:
        form = MiembroForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                try:
                    user = User.objects.get(email=form.cleaned_data['mail'])
                except:
                    user = None
                if user == None:
                    username = str(form.cleaned_data['mail']).split('@')[0]
                    aux = 0
                    while (user == None):
                        try:
                            if aux == 0:
                                user = User.objects.get(username=username)
                                user = None
                            else:
                                user = User.objects.get(username=username+str(aux))
                                user = None
                        except:
                            if aux == 0:
                                user = User.objects.create_user(username, form.cleaned_data['mail'], 'sistema-mu')
                            else:
                                user = User.objects.create_user(username+str(aux), form.cleaned_data['mail'], 'sistema-mu')
                            print get_current_site(request)
                            token= signing.dumps(user.pk,salt="password_recovery")

                            subject,from_mail, to = 'Sistema MU','gmacchi@bellbird.com.py', user.email
                            html_content = '<p>Bienvenido al Sistema MU, se creo una cuenta suya para participar en el establecimiento <strong>'+str(establecimiento.nombre)+ '</strong>.</p>' +'<p>Por favor accede a este <a href="http://'+str(get_current_site(request))+'/password/reset/'+str(token)+'"> link</a> para asginar una contraseña.</p>'
                            msg = EmailMessage(subject, html_content,from_mail, [to])
                            msg.content_subtype = "html"  # Main content is now text/html
                            msg.send()
                        aux +=1
                establecimiento.miembros.add(user)
                establecimiento.save()
                return redirect('/establecimiento/detail/'+str(establecimiento.id)+'/')
            else:
                return render(request, 'add_miembro.html', {'form': form})

        return render(request,'add_miembro.html',{'form':form})


class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter)
    filter_fields = ('establecimiento','leido',)
    ordering_fields = '__all__'
    ordering = ('fecha',)

class UsuariosEstablecimientoViewSet(viewsets.ViewSet):

    def list(self, request, format=None):
        if (request.query_params):
            results = []
            owner_in = False
            establecimiento = Establecimiento.objects.get(pk=request.query_params.get('establecimiento'))
            miembros = establecimiento.miembros.all().values()
            for usuario in miembros:
                results.append({'username': usuario['username'], 'id': usuario['id']})
                if usuario['id'] == establecimiento.owner_id:
                    owner_in = True
            if not owner_in:
                results.append({'username': establecimiento.owner.username, 'id': establecimiento.owner_id})
            response = {'lista': results}
        else:
            response = {'lista': None}
        return Response(response)
