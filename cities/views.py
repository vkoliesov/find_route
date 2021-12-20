from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import City
from .forms import CityForm

class CityListView(generic.ListView):
    model = City
    paginate_by = 3
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


class CityCreateView(SuccessMessageMixin, generic.CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:cities_list')
    success_message = "City was created successfully"


class CityUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:cities_list')
    success_message = "City was updated successfully"


class CityDeleteView(generic.DeleteView):
    model = City
    # form_class = CityForm
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:cities_list')
    success_message = "City was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(self, request, *args, **kwargs)