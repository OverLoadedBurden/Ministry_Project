from .views import *
from django.conf.urls import url

urlpatterns = [
    url('all', get_univs),
    url('create', create),
    url(r'^delete/', delete),
    url(r'^adjust/(?P<id>\d)', adjust),
]
