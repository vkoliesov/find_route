from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import Route
from .forms import RouteForm
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


class RouteListView(generic.ListView):
    model= Route
    template_name = 'routes/home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RouteForm()
        context['form'] = form
        return context
