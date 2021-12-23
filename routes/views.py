from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Route
from .forms import RouteForm

class RouteListView(generic.ListView):
    model= Route
    template_name = 'routes/home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RouteForm()
        context['form'] = form
        return context