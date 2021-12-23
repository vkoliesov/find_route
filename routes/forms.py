from django import forms

from .models import Route
from cities.models import City


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(label='From', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-example-basic-single',
    }))

    to_city = forms.ModelChoiceField(label='To', queryset=City.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control js-example-basic-single',
    }))
    cities = forms.ModelMultipleChoiceField(label='Through the cities', queryset=City.objects.all(),
        required=False, widget=forms.SelectMultiple(attrs={ 
        'class' : 'form-control js-example-basic-multiple'
    }))
    traveling_time = forms.IntegerField(label='Travel time', widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'placeholder': 'Travel time'
    }))