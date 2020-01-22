from .models import *
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^by_name/', by_name),
    url(r'^by_std/(?P<std>\d)', by_std),
    url(r'^delete/(?P<id>\d)', delete),
    url(r'^by_unv/', by_unv),
    url('all/', all),
    url('create/', create),
    ]
