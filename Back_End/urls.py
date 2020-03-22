"""Back_End URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.http import HttpResponse
from django.urls import path
from users.models import User
from json import loads, dumps


def auth(name, password):
    ret = 2
    u = None
    try:
        u = User.objects.get(['name', name])
        ret -= 1
        if u.password == password:
            ret -= 1
    except Exception:
        pass
    return HttpResponse(ret)


def get_user(request):
    return HttpResponse(dumps(User.objects.get(['name', request.GET.get('name')]).serialize()))


def auth_route(request):
    dic = loads(request.body.decode('UTF-8'))
    return auth(name=dic['name'], password=dic['password'])


def create(request):
    dic = loads(request.body.decode('UTF-8'))
    from users.models import User
    User.objects.create(
        name=dic['name'],
        password=dic['password'],
        isAdmin=dic['isAdmin']
    ).save()
    return HttpResponse(0)


urlpatterns = [
    path('admin/', admin.site.urls),
    url('research/', include('Research.urls')),
    url('std/', include('Students.urls')),
    url('auth/', auth_route),
    url('get_user/', get_user),
    url('create/', create),
]
