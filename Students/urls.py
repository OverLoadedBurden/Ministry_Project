from .views import *
from django.conf.urls import url

urlpatterns = [
    url('create/', create),
    url('(?P<id>\d)', search),
    # url('create/', create)
]
