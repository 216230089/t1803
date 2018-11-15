from django.conf.urls import url
from cpr.views import *

urlpatterns = [
    # /cpr
    url(r'^$', CprLV.as_view(), name='index'),
    # url(r'^bookmark/adult/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='adult',
    url(r'^$', CprDV.as_view(), name='detail'

    ),

    # Example: /add/
    url(r'^add/$',
        CprCreateView.as_view(), name="add",
    ),

    # Example: /change/
    url(r'^change/$',
        CprChangeLV.as_view(), name="change",
    ),

    # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$',
        CprUpdateView.as_view(), name="update",
    ),

    # Example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',
        CprDeleteView.as_view(), name="delete",
    ),
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