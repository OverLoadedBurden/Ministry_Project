from django.shortcuts import render, HttpResponse
from json import loads, dumps
from Students.models import Student
from University.models import University
from base64 import b64encode, encodebytes,b64decode


# Create your views here.
def search(request, id):
    # try:
    def converter(o:bytes):
        # o.title()
        # b64decode(o.hex())
        o.tit
        return f'{o.decode(encoding="ascii")}'

    s = Student.objects.get(collage_no=id)
    joins = ['university']
    return HttpResponse(dumps(s.serialize(*joins), default=converter))


# except Exception:
#     return HttpResponse('1')


def create(request):
    dic = loads(request.body.decode('UTF-8'))
    Student.objects.create(
        collage_no=dic['no'],
        name=dic['name'],
        ph=dic['ph'],
        university=University.objects.get(['name', dic['uni']])
    ).save()
    return HttpResponse(0)
