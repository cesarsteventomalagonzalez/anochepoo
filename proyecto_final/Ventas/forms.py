from django import forms
from django.forms import ModelForm

from Ventas.models import *


# class CategoriaForm(forms.ModelForm):
#     class Meta:
#         model = Categoria
#         fields = ['descripcion', 'estado']
#         widgets = {
#             'descripcion': forms.TextInput(attrs={
#                 'placeholder': 'Ingrese la linea de prooductos',
#                 'class': 'form-group',
#                 'required': True,
#             })
#
#         }
#
# class ProductosForm(forms.ModelForm):
#     class Meta:
#         model = Productos
#         fields = ['nombre', 'categoria', 'estado']
#         widgets = {
#             'nombre': forms.TextInput(attrs={
#                 'placeholder': 'Ingrese el nombre',
#                 'class': 'form-group',
#                 'required': True
#             }),
#
#             'categoria': forms.Select(attrs={
#                 'class': 'form-group',
#                 'required': True
#             }),
#         }


class PostulanteForm(ModelForm):
    class Meta:
        model = Postulante
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Nombres'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese correo'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese de telefono'}),

        }



