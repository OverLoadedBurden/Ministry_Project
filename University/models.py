from django.db import models
from django_serializable_model import SerializableModel


# Create your models here.
class University(SerializableModel):
    name = models.TextField(primary_key=True)
    desc = models.TextField()
    image = models.BinaryField()

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.TextField()
    degree = models.TextField()
