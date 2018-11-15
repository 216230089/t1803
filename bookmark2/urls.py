from django.conf.urls import url
from bookmark2.views import *

urlpatterns = [
    # /bookmark2
    url(r'^$', BookmarkLV2.as_view(), name='index2'),
    # url(r'^bookmark/adult/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='adult',
    url(r'^$', BookmarkDV2.as_view(), name='detail2'

    ),

    # Example: /add2/
    url(r'^add2/$',
        BookmarkCreateView2.as_view(), name="add2",
    ),

    # Example: /change2/
    url(r'^change2/$',
        BookmarkChangeLV2.as_view(), name="change2",
    ),

    # Example: /99/update2/
    url(r'^(?P<pk>[0-9]+)/update2/$',
        BookmarkUpdateView2.as_view(), name="update2",
    ),

    # Example: /99/delete2/
    url(r'^(?P<pk>[0-9]+)/delete2/$',
        BookmarkDeleteView2.as_view(), name="delete2",
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