from django.shortcuts import render, HttpResponse
from django.core.serializers import serialize
from json import loads
from base64 import b64decode
from .models import University


# Create your views here.
def get_univs(request):
    return HttpResponse(serialize('json', University.objects.all()))


def delete(request):
    id = request.GET.get('id')
    University.objects.get(['name', id]).delete()
    return HttpResponse(0)


def create(request):
    dic = loads(request.body.decode('UTF-8'))
    if not dic.__contains__('id'):
        University.objects.create(name=dic['name'], desc=dic['desc'], image=b64decode(dic['img'])).save()
    else:
        u = University.objects.get(['name', dic['id']])
        u.name = dic['name']
        u.desc = dic['desc']
        u.image = b64decode(dic['img'])
        u.save()
    return HttpResponse(0)


def adjust(request):
    dic = loads(request.body.decode('UTF-8'))
    uni = University.objects.get(dic['id'])
    uni.name = dic['name']
    uni.programs = dic['programs']
    uni.image = dic['image']
    uni.save()
    return HttpResponse(0)
