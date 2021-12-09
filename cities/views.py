from django.shortcuts import get_object_or_404
from django.views import generic
from .models import City


class CityListView(generic.ListView):
    model = City
    template_name = 'cities/home.html'
    



class CityDetailView(generic.DetailView):
    template_name = 'cities/detail.html'

    def get_object(self):
        return get_object_or_404(City, pk=self.kwargs.get('city_id'))