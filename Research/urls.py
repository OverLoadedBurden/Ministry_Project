from .models import *
from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^by_name/', by_name),
    url(r'^by_std/', by_std),
    url(r'^delete/(?P<id>\d)', delete),
    url(r'^by_unv/', by_unv),
    url('all/', all),
    url('create/', create),
    url('by_degree_and_user', by_degree_and_user),
    url('by_degree', by_degree)
]
