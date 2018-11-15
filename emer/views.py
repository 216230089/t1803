from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from emer.models import Emer
# from emer.models import City
# from tagging.models import Tag, TaggedItem
# from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from emer.forms import EmerSearchForm
from django.db.models import Q
from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

# Create your views here.

class EmerLV(ListView):
    model = Emer
    template_name = 'emer/emer_list.html'
    context_object_name = 'emers'
    paginate_by = 6



class EmerDV(DetailView):
    model = Emer

class EmerCreateView(LoginRequiredMixin, CreateView):
    model = Emer
    fields = ['mname', 'madd', 'mtel']
    success_url = reverse_lazy('emer:index')

    def form_valid(self, form):
        form.instance.mname = self.request.user
        return super(EmerCreateView, self).form_valid(form)

class EmerChangeLV(LoginRequiredMixin, ListView):
    template_name = 'emer/emer_change_list.html'

    def get_queryset(self):
        return Emer.objects.filter(mname=self.request.user)

class EmerUpdateView(LoginRequiredMixin, UpdateView) :
    model = Emer
    fields = ['mname', 'madd', 'mtel']
    success_url = reverse_lazy('emer:index')

class EmerDeleteView(LoginRequiredMixin, DeleteView) :
    model = Emer
    success_url = reverse_lazy('emer:index')

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
class BstrapSearchLV(ListView) :
    template_name = 'emer/emer_bstrap_search.html'

    def get_queryset(self):
        schWord = '%s' % self.request.GET['search']
        emer_list = Emer.objects.filter(Q(mname__icontains=schWord) | Q(madd__icontains=schWord) | Q(mtel__icontains=schWord)).distinct()
        self.search_term = schWord
        self.count = emer_list.count()
        return emer_list

    def get_context_data(self, **kwargs):
        context = super(BstrapSearchLV, self).get_context_data(**kwargs)
        context['search_term'] = self.search_term
        context['search_count'] = self.count
        return context

#--- FormView
class SearchFormView(FormView):
    form_class = EmerSearchForm
    template_name = 'emer/emer_search.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']
        emer_list = Emer.objects.filter(Q(mname__icontains=schWord) | Q(mtel__icontains=schWord) | Q(madd__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = emer_list

        return render(self.request, self.template_name, context)

#--- ArchiveView
class EmerAV(ArchiveIndexView) :
    model = Emer
    date_field = 'mname'

class EmerYAV(YearArchiveView) :
    model = Emer
    date_field = 'mname'
    make_object_list = True

class EmerMAV(MonthArchiveView) :
    model = Emer
    date_field = 'mname'

class EmerDAV(DayArchiveView) :
    model = Emer
    date_field = 'mname'

class EmerTAV(TodayArchiveView) :
    model = Emer
    date_field = 'mname'
