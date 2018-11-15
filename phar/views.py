from django.shortcuts import render

from django.views.generic import ListView, DetailView
from phar.models import Phar

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class PharLV(ListView):
    model = Phar

class PharDV(DetailView):
    model = Phar

class PharCreateView(LoginRequiredMixin, CreateView):
    model = Phar
    fields = ['title', 'url']
    success_url = reverse_lazy('phar:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PharCreateView, self).form_valid(form)

class PharChangeLV(LoginRequiredMixin, ListView):
    template_name = 'phar/phar_change_list.html'

    def get_queryset(self):
        return Phar.objects.filter(owner=self.request.user)

class PharUpdateView(LoginRequiredMixin, UpdateView) :
    model = Phar
    fields = ['title', 'url']
    success_url = reverse_lazy('phar:index')

class PharDeleteView(LoginRequiredMixin, DeleteView) :
    model = Phar
    success_url = reverse_lazy('phar:index')

