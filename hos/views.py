from django.shortcuts import render

from django.views.generic import ListView, DetailView
from hos.models import Hos

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class HosLV(ListView):
    model = Hos

class HosDV(DetailView):
    model = Hos

class HosCreateView(LoginRequiredMixin, CreateView):
    model = Hos
    fields = ['title', 'url']
    success_url = reverse_lazy('hos:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(HosCreateView, self).form_valid(form)

class HosChangeLV(LoginRequiredMixin, ListView):
    template_name = 'hos/hos_change_list.html'

    def get_queryset(self):
        return Hos.objects.filter(owner=self.request.user)

class HosUpdateView(LoginRequiredMixin, UpdateView) :
    model = Hos
    fields = ['title', 'url']
    success_url = reverse_lazy('hos:index')

class HosDeleteView(LoginRequiredMixin, DeleteView) :
    model = Hos
    success_url = reverse_lazy('hos:index')

