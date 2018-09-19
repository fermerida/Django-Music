# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect	
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail

import os
import csv
import subprocess
import cx_Oracle
import datetime
import sys

from myapp.forms import *


# Create your views here.



def index(request):
    return render(request, 'index.html')


def login(request):
    # This view is missing all form handling logic for simplicity of the example
    form = loginForm(request.POST)
    variables={
        "form":form,
    }

    if form.is_valid():
      
        datos = form.cleaned_data
        user = datos.get("usuario")
        psw = datos.get("password")
        connection = cx_Oracle.connect("MIA/stark@localhost/XE")
        cursor= connection.cursor()
        cursor.execute('select USUARIO, CLAVE, TIPO from USUARIO')
        for row in cursor:     
            print (row[2], sys.stderr)    
            if user == row[0] and psw == row[1]:
                #usuario = auth.authenticate(username = user, password = psw)
                #auth.login(request, usuario)
                if row[2]== 1:
                    return render(request, 'admin.html', {'user': user})
                elif row[2]== 2:
                    return render(request, 'empleado.html', {'user': user})
                elif row[2]== 3:
                    return render(request, 'cliente.html', {'user': user})
                   #return render(request, 'clienteme.html', {'user': user})
                elif row[2]== 4:
                    return render(request, 'frozen.html', {'user': user})
                else:
                    return render(request, 'frozen.html', {'user': user})

    return render(request, 'login.html', {'form': loginForm()})

def registro(request):
    form = registroForm(request.POST or None, request.FILES or None)
    variables={
        "form":form,
    }

    if form.is_valid():        
        datos = form.cleaned_data
        usuario = datos.get("username")
        contra = datos.get("password")
        mail = datos.get("email")
        nombre = datos.get("nombre")
        lastname = datos.get("apellido")
        fecha_registro = datetime.date.today()
        rol = 3
        foto = request.FILES['photo']
        file_type = foto.name.split('.')[-1]
        file_type = file_type.lower()

        path = '/home/fer/django-apps/miaproject2/myapp/media/' + usuario +'.' + file_type
        handle_uploaded_file(foto,path)

        connection = cx_Oracle.connect("MIA/stark@localhost/XE")
        cursor= connection.cursor()


        statement2 = 'insert into USUARIO(USUARIO, CORREO, NOMBRE, APELLIDO, FOTO, TIPO, CLAVE, FECHA_REGISTRO) values(:2, :3, :4, :5, :6, :7, :8, :9)'
        cursor.execute(statement2, (usuario, mail, nombre, lastname,path, rol, contra, fecha_registro))
        connection.commit()
        return render(request, 'admin.html', {'form': registroForm()})
    return render(request, 'registro.html', {'form': registroForm()})

def handle_uploaded_file(f,path):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def administrar(request):
    return render(request, 'admin.html')