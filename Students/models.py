from django.db import models
from University.models import University
from django_serializable_model import SerializableModel


# Create your models here.
class Student(SerializableModel):
    collage_no = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)
    ph = models.IntegerField(unique=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
