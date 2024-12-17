from django import forms
from .models import Plato

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre', 'precio']


    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
