from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^list_caravana/(\d+)/$', list_caravana_animal),
]