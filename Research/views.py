from django.shortcuts import render, HttpResponse
from .models import Research
from Students.models import Student
from json import loads, dumps
from base64 import b64decode, b64encode
from django.core.serializers import serialize
from users.models import User


# Create your views here.
def serialize_collection(collection):
    def converter(object):
        return object.__str__()

    joins = ['student_set']
    l = []
    for i in collection:
        d = i.serialize(*joins)
        res = d['research']
        del d['research']
        if res is not None:
            # /////
            d['research'] = b64encode(res).decode('UTF-8')
        l.append(d)
    return dumps(l, default=converter)


def all(request):
    return HttpResponse(serialize_collection(Research.objects.all()))


def by_name(request):
    title = request.GET.get('title')
    return HttpResponse(serialize_collection(Research.objects.filter(title__contains=title)))


def byType(request):
    type = request.GET.get('type')
    return HttpResponse(serialize_collection(Research.objects.filter(type=type)))


def by_type(request):
    type = request.GET.get('type')
    return HttpResponse(serialize_collection(Research.objects.filter(type__contains=type)))


def search(request):
    # def serialize_collection(collection):
    #     def converter(object):
    #         if type(object) is bytes:
    #             return None
    #         return object.__str__()
    #
    #     joins = ['student_set']
    #     l = []
    #     for i in collection:
    #         l.append(i.serialize(*joins))
    #     return dumps(l, default=converter)

    map = loads(request.body.decode('UTF-8'))
    # first search the name
    rs = Research.objects.filter(title__contains=map['name'])
    # add the results to the manipulated set
    l = [*rs]

    # second search the type if the type is not any
    if map['type'] != 'any':
        rs = rs.filter(type__contains=map['type'])

    # third part is to remove any element that does not have  meet the number condition
    if map['no'] == 0:
        # return HttpResponse(len(l))
        return HttpResponse(serialize_collection(l))
    for r in l:
        if map['op'] == 0:
            if r.student_set.count() != map['no']:
                l.remove(r)
        if map['op'] == 1:
            if r.student_set.count() >= map['no']:
                l.remove(r)
        if map['op'] == 2:
            if r.student_set.count() <= map['no']:
                l.remove(r)
    # return HttpResponse(len(l))
    return HttpResponse(serialize_collection(l))


def delete(request, id):
    # print(id)
    # return HttpResponse(id)
    Research.objects.get(id=id).delete()
    return HttpResponse(0)


def create(request):
    dic = loads(request.body.decode('UTF-8'))
    set = []
    for s in dic['stds']:
        set.append(Student.objects.get(pk=s))
    r = Research.objects.create(title=dic['title'], type=dic['type'], research=b64decode(dic['research']))
    r.save()
    r.student_set.add(*set)
    r.save()
    return HttpResponse('0')
