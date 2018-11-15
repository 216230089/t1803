from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from sigudong.models import Sigudong
# from emer.models import City
# from tagging.models import Tag, TaggedItem
# from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
# from city.forms import CitySearchForm
from django.db.models import Q
from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class SigudongLV(ListView):
    model = Sigudong
    template_name = 'sigudong/sigudong_list.html'
    context_object_name = 'sigudongs'
    paginate_by = 6



class SigudongDV(DetailView):
    model = Sigudong

class SigudongCreateView(LoginRequiredMixin, CreateView):
    model = Sigudong
    fields = ['si', 'gu', 'dong']
    success_url = reverse_lazy('sigudong:index')

    def form_valid(self, form):
        form.instance.si = self.request.user
        return super(SigudongCreateView, self).form_valid(form)

class SigudongChangeLV(LoginRequiredMixin, ListView):
    template_name = 'sigudong/sigudong_change_list.html'

    def get_queryset(self):
        return Sigudong.objects.filter(si=self.request.user)

class SigudongUpdateView(LoginRequiredMixin, UpdateView) :
    model = Sigudong
    fields = ['si', 'gu', 'dong']
    success_url = reverse_lazy('sigudong:index')

class SigudongDeleteView(LoginRequiredMixin, DeleteView) :
    model = Sigudong
    success_url = reverse_lazy('sigudong:index')

# def emer_list(request):
#     qs = Emer.objects.all()

#     q = request.GET.get('q', '') #GET request의 인자중에 q값이 있으면 가져오고, 없으면 빈 문자열 넣기

#     if q: #q가 있으면
#         qs = qs.filter(title__icontains=q)  #베목에 q가 포함되어 있는 레코드만 필터링

#         return render(request, 'emer/emer_search.html', {
#             'emer_search' : qs,
#             'q' : q,
#         })

#--- Bootstrap Search Result
# class BstrapSearchLV(ListView) :
#     template_name = 'city/city_bstrap_search.html'

#     def get_queryset(self):
#         schWord = '%s' % self.request.GET['search']
#         city_list = City.objects.filter(Q(si__icontains=schWord) | Q(gu__icontains=schWord) | Q(dong__icontains=schWord)).distinct()
#         self.search_term = schWord
#         self.count = city_list.count()
#         return city_list

#     def get_context_data(self, **kwargs):
#         context = super(BstrapSearchLV, self).get_context_data(**kwargs)
#         context['search_term'] = self.search_term
#         context['search_count'] = self.count
#         return context

# #--- FormView
# class SearchFormView(FormView):
#     form_class = CitySearchForm
#     template_name = 'city/city_search.html'

#     def form_valid(self, form) :
#         schWord = '%s' % self.request.POST['search_word']
#         city_list = City.objects.filter(Q(si__icontains=schWord) | Q(gu__icontains=schWord) | Q(dong__icontains=schWord)).distinct()

#         context = {}
#         context['form'] = form
#         context['search_term'] = schWord
#         context['object_list'] = emer_list

#         return render(self.request, self.template_name, context)

#--- ArchiveView
class SigudongAV(ArchiveIndexView) :
    model = Sigudong
    date_field = 'si'

class SigudongYAV(YearArchiveView) :
    model = Sigudong
    date_field = 'si'
    make_object_list = True

class SigudongMAV(MonthArchiveView) :
    model = Sigudong
    date_field = 'si'

class SigudongDAV(DayArchiveView) :
    model = Sigudong
    date_field = 'si'

class SigudongTAV(TodayArchiveView) :
    model = Sigudong
    date_field = 'si'
