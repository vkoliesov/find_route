from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from trains.models import Train
from cities.models import City

from .models import Route
from .forms import RouteForm, RouteModelForm
from .utils import get_routes


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            return render(request, 'routes/home.html', context=context)
    else:
        form = RouteForm()
        messages.error(request, "No data to search")
    return render(request, 'routes/home.html', {'form': form})

def add_route(request):
    if request.method == 'POST':
        context = {}
        data = request.POST
        if data:
            total_time = int(data['total_time'])
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            trains = data['trains'].split(',')
            trains_lst = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_lst).select_related('from_city', 'to_city')
            cities = City.objects.filter(id__in=[from_city_id, to_city_id]).in_bulk()
            form = RouteModelForm(
                initial={
                    'from_city': cities[from_city_id],
                    'to_city': cities[to_city_id],
                    'travel_times': total_time,
                    'trains': qs
                    })
            context['form'] = form

        return render(request, 'routes/create.html', context=context)
    else:
        messages.error(request, "Cannot save non-existent route")
    return redirect('/routes')


def save_route(request):
    if request.method == 'POST':
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The route is saved successfully")
            return redirect('/routes')
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, "Cannot save non-existent route")
    return redirect('/routes')


class RouteFindView(generic.ListView):
    model= Route
    template_name = 'routes/home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RouteForm()
        context['form'] = form
        return context


class RouteListView(generic.ListView):
    model = Route
    template_name = 'routes/list.html'
    paginate_by = 5


class RouteDetailView(generic.DetailView):
    template_name = 'routes/detail.html'

    def get_object(self):
        return get_object_or_404(Route, pk=self.kwargs.get('pk'))