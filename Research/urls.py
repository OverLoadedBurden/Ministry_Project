from .models import *
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^by_name/', by_name),
    url(r'^delete/(?P<id>\d)', delete),
    url('all/', all),
    url('create/', create),
    url('search', search),
    url('byType', byType)
]
