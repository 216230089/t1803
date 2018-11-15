from django.shortcuts import render

from django.views.generic import ListView, DetailView
from ambulance.models import Ambulance

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class AmbulanceLV(ListView):
    model = Ambulance

class AmbulanceDV(DetailView):
    model = Ambulance

class AmbulanceCreateView(LoginRequiredMixin, CreateView):
    model = Ambulance
    fields = ['title', 'url']
    success_url = reverse_lazy('ambulance:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(AmbulanceCreateView, self).form_valid(form)

class AmbulanceChangeLV(LoginRequiredMixin, ListView):
    template_name = 'ambulance/ambulance_change_list.html'

    def get_queryset(self):
        return Ambulance.objects.filter(owner=self.request.user)

class AmbulanceUpdateView(LoginRequiredMixin, UpdateView) :
    model = Ambulance
    fields = ['title', 'url']
    success_url = reverse_lazy('ambulance:index')

class AmbulanceDeleteView(LoginRequiredMixin, DeleteView) :
    model = Ambulance
    success_url = reverse_lazy('ambulance:index')

