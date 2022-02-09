from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Train
from .forms import TrainForm

class TrainListView(generic.ListView):
    model = Train
    paginate_by = 3
    template_name = 'trains/home.html'


class TrainDetailView(generic.DetailView):
    template_name = 'trains/detail.html'

    def get_object(self):
        return get_object_or_404(Train, pk=self.kwargs.get('pk'))


class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:trains_list')
    success_message = "Train was created successfully"


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:trains_list')
    success_message = "Train was updated successfully"


class TrainDeleteView(LoginRequiredMixin,generic.DeleteView):
    model = Train
    # form_class = TrainForm
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:trains_list')
    success_message = "Train was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(self, request, *args, **kwargs)