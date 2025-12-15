from django import forms   #importa el módulo de formularios de Django
from .models import Pedido #importa el modelo Pedido desde el archivo models.py en el mismo directorio

class PedidoForm(forms.ModelForm):  #cambio 1. se crea un formulario basado en el modelo Pedido
    class Meta:
        model = Pedido
        fields = ['cliente', 'fecha_pedido', 'producto', 'cantidad', 'estado']    #lista de campos del modelo que se incluirán en el formulario
        widgets = {  #cambio 1. se agregan clases de bootstrap a los campos del formulario
            'fecha_pedido': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'producto': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }