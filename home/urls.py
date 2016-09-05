from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', home),
    url(r'^sistema/$', index),
    url(r'^login/',login_view),
    url(r'^logout/',logout_view),
    url(r'^register/', register_view),
    url(r'^cuenta/',cuenta_view),
    url(r'^pricing/',pricing_view),
    url(r'^contact/', contact_view)

]