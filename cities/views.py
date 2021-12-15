from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import City
from .forms import CityForm

class CityListView(generic.ListView):
    model = City
    template_name = 'cities/home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = CityForm()
        context['form'] = form
        return context
    


class CityDetailView(generic.DetailView):
    template_name = 'cities/detail.html'

    def get_object(self):
        return get_object_or_404(City, pk=self.kwargs.get('pk'))


class CityCreateView(generic.CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:cities_list')


class CityUpdateView(generic.UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:cities_list')


class CityDeleteView(generic.DeleteView):
    model = City
    # form_class = CityForm
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:cities_list')