from django import forms
from django.forms.widgets import Select

from .models import Train
from cities.models import City


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Train number', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the train number'
        }))
    travel_time = forms.IntegerField(label='Travel time', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Travel time'
    }))

    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))

    to_city = forms.ModelChoiceField(label='To', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
    }))
    
    class Meta:
        model = Train
        fields = '__all__'