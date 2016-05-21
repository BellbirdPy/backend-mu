from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^add/',add_view),
    url(r'^detail/(\d+)/$', detail_view),
    url(r'^delete/(\d+)/$', delete_view),
    url(r'^(\d+)/miembro/delete/(\d+)/$', delete_miembro_view),
    url(r'^(\d+)/miembro/add/$', add_miembro_view),
]