from django.db import models
from django_serializable_model import SerializableModel
from Research.models import Research


# Create your models here.
class Student(SerializableModel):
    collage_no = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)
    ph = models.IntegerField(unique=True)
    research = models.ForeignKey(Research, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
