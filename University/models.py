from django.db import models


# Create your models here.
class University(models.Model):
    name = models.TextField()
    programs = models.TextField()
    image = models.BinaryField()


class Program(models.Model):
    name = models.TextField()
    degree = models.TextField()
