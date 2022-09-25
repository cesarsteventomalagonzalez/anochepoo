from django.forms import ModelForm
from django import forms
from Ventas.models import Postulante


class PostulanteForm(ModelForm):
    class Meta:
        model = Postulante
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Apellidos'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese correo'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese de telefono'}),

        }


