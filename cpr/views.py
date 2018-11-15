from django.shortcuts import render

from django.views.generic import ListView, DetailView
from cpr.models import Cpr

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class CprLV(ListView):
    model = Cpr

class CprDV(DetailView):
    model = Cpr

class CprCreateView(LoginRequiredMixin, CreateView):
    model = Cpr
    fields = ['title', 'url']
    success_url = reverse_lazy('cpr:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CprCreateView, self).form_valid(form)

class CprChangeLV(LoginRequiredMixin, ListView):
    template_name = 'cpr/cpr_change_list.html'

    def get_queryset(self):
        return Cpr.objects.filter(owner=self.request.user)

class CprUpdateView(LoginRequiredMixin, UpdateView) :
    model = Cpr
    fields = ['title', 'url']
    success_url = reverse_lazy('cpr:index')

class CprDeleteView(LoginRequiredMixin, DeleteView) :
    model = Cpr
    success_url = reverse_lazy('cpr:index')

