# -*- coding: utf-8 -*-
from django import forms
import cx_Oracle 

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class loginForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)

class registroForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    email = forms.CharField(widget=forms.TextInput,required=True)
    nombre = forms.CharField(widget=forms.TextInput,required=True)
    apellido = forms.CharField(widget=forms.TextInput,required=True)
    foto = forms.FileField(required=False)

