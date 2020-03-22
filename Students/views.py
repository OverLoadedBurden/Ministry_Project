from django.shortcuts import render, HttpResponse
from json import loads, dumps
from Students.models import Student
from django.core.serializers import serialize
from base64 import b64encode, encodebytes, b64decode


# Create your views here.
def search(request):
    collage_no = request.GET.get('no')
    type = request.GET.get('type')
    name = request.GET.get('name')
    s = None
    if type == '0':
        s = Student.objects.filter(collage_no__contains=collage_no, name__contains=name)
    if type == '1':
        s = Student.objects.filter(collage_no__contains=collage_no, name__contains=name, research__isnull=False)
    if type == '2':
        s = Student.objects.filter(collage_no__contains=collage_no, name__contains=name, research__isnull=True)
    return HttpResponse(dumps(s.serialize()))


def delete(request):
    s = Student.objects.get(collage_no=request.GET.get('id'))
    s.delete()
    return HttpResponse(0)


# except Exception:
#     return HttpResponse('1')


def create(request):
    dic = loads(request.body.decode('UTF-8'))
    try:
        Student.objects.create(
            collage_no=dic['no'],
            name=dic['name'],
            ph=dic['ph'],
        ).save()
        return HttpResponse(0)
    except:
        return HttpResponse(1)


def byName(request):
    return HttpResponse(serialize('json', Student.objects.filter(name__contains=request.GET.get('name'))))

def byID(request):
    return HttpResponse(serialize('json', Student.objects.filter(pk__contains=request.GET.get('id'))))


def all(request): return HttpResponse(dumps(Student.objects.all().serialize()))


def available(request): return HttpResponse(dumps(Student.objects.filter(research=None).serialize()))
