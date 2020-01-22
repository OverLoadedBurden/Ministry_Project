from django.shortcuts import render, HttpResponse
from .models import Research
from Students.models import Student
from json import loads, dumps
from django.core.serializers import serialize
from University.models import University
from users.models import User


#
# def get_research_dict(res: Research) -> dict:
#     res.__dict__


# Create your views here.
def serialize_collection(collection):
    def converter(object):
        return object.__str__()

    joins = ['std', 'user', 'unv']
    return dumps(collection.serialize(*joins), default=converter)


def all(request):
    return HttpResponse(serialize_collection(Research.objects.all()))


def by_std(request, std):
    std = Student.objects.get(['collage_no', std])
    return HttpResponse(serialize_collection(Research.objects.filter(['std', std])))


def by_unv(request):
    unv = request.GET.get('unv')
    unv = University.objects.get(['name', unv])
    return HttpResponse(serialize_collection(Research.objects.filter(['unv', unv])))
    # print(unv)
    return HttpResponse(unv)


def by_name(request):
    title = request.GET.get('title')
    return HttpResponse(serialize_collection(Research.objects.filter(title__contains=title)))
    # print('name=\'' + title + '\'')
    # return HttpResponse(title)


def delete(request, id):
    Research.objects.get(['id', id]).delete()
    return HttpResponse(0)


def create(request):
    dic = loads(request.body.decode('UTF-8'))
    if not dic.__contains('id'):
        try:
            Research.objects.create(title=dic['title'], abstract=dic['abstract'],
                                    unv=University.objects.get(['name', dic['univ']]),
                                    std=Student.objects.get(['collage_no', dic['std']]),
                                    user=User.objects.get(['name', dic['user']])).save()
            return HttpResponse(0)
        except Exception:
            return HttpResponse(1)
    else:
        try:
            r = Research.objects.get(['id', dic['id']])
            r.title = dic['title']
            r.abstract = dic['abstract']
            r.unv = University.objects.get(['name', dic['univ']])
            r.std = Student.objects.get(['collage_no', dic['std']])
            r.user = User.objects.get(['name', dic['user']])
            r.save()
            return HttpResponse(10)
        except Exception:
            return HttpResponse(11)
