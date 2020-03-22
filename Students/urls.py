from .views import *
from django.conf.urls import url

urlpatterns = [
    url('create/', create),
    url('byName', byName),
    url('byID', byID),
    url('search/', search),
    url('delete/', delete),
    url('all/', all),
    url('available/', available)
]
