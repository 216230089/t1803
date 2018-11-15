from django.conf.urls import url
from sigudong.views import *

urlpatterns = [
    # /city
    url(r'^$', SigudongLV.as_view(), name='index'),
    # url(r'^bookmark/adult/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='adult',
    url(r'^$', SigudongDV.as_view(), name='detail'),

    # Example: /add/
    url(r'^add/$',
        SigudongCreateView.as_view(), name="add",
    ),

    # Example: /change/
    url(r'^change/$',
        SigudongChangeLV.as_view(), name="change",
    ),

    # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$',
        SigudongUpdateView.as_view(), name="update",
    ),

    # Example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',
        SigudongDeleteView.as_view(), name="delete",
    ),

        # Example: /search/
    # url (r'^search/$', SearchFormView.as_view(), name='search'),

    # # Example: /bssearch/ (Bootstrap Search)
    # url (r'^bssearch/$', BstrapSearchLV.as_view(), name='bssearch'),

     # Example: /archive/
    url(r'^archive/$', SigudongAV.as_view(), name='city_archive'),

    # Example: /2012/
    url(r'^(?P<year>\d{4})/$', SigudongYAV.as_view(), name='city_year_archive'),

    # Example: /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', SigudongMAV.as_view(), name='city_month_archive'),

    # Example: /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', SigudongDAV.as_view(), name='city_day_archive'),

    # Example: /today/
    url(r'^today/$', SigudongTAV.as_view(), name='city_today_archive'),

]


# from django.conf.urls import url
# from bookmark2.views import *

# urlpatterns = [
#     # url(r'^$', views.bookmark2_list, name='index'),
#     url(r'^$', BookmarkLV2.as_view(), name='index2'),
#     url(r'^$', BookmarkDV2.as_view(), name='detail2'),
#     # url(r'^bookmark2/(?P<pk>\d+)/$', views.bookmark2_detail, name='bookmark2_detail'),

#     # def bookmark2_detail(request, pk):
#     # bookmark2 = get_object_or_404(Bookmark2, pk=pk)
#     # return render(request, 'bookmark2/post_detail.html', {'post': post})

#     # Example: /add2/
#     url(r'^add2/$',
#         BookmarkCreateView2.as_view(), name="add2",
#     ),

#     # Example: /change2/
#     url(r'^change2/$',
#         BookmarkChangeLV2.as_view(), name="change2",
#     ),

# ]