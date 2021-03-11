from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from trains.models import Train
from trains.forms import TrainForm


class TrainListView(ListView):
    model = Train
    template_name = 'trains/home.html'
    paginate_by = 5



class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'

    # def get_queryset(self):
    #     return get_object_or_404(Train, pk=self.kwargs.get('pk'))


class TrainCreateView(CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Train was created successfully"


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Train was edited successfully"


class TrainDeleteView(DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.error(request, 'Train deleted.')
        return self.post(request, *args, **kwargs)
