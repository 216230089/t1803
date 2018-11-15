from django.shortcuts import render

from django.views.generic import ListView, DetailView
from bookmark2.models import Bookmark2

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class BookmarkLV2(ListView):
    model = Bookmark2

class BookmarkDV2(DetailView):
    model = Bookmark2

class BookmarkCreateView2(LoginRequiredMixin, CreateView):
    model = Bookmark2
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookmarkCreateView2, self).form_valid(form)

class BookmarkChangeLV2(LoginRequiredMixin, ListView):
    template_name = 'bookmark2/bookmark2_change_list.html'

    def get_queryset(self):
        return Bookmark2.objects.filter(owner=self.request.user)

class BookmarkUpdateView2(LoginRequiredMixin, UpdateView) :
    model = Bookmark2
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark2:index2')

class BookmarkDeleteView2(LoginRequiredMixin, DeleteView) :
    model = Bookmark2
    success_url = reverse_lazy('bookmark2:index2')

