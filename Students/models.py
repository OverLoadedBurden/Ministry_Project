from django.db import models
from University.models import University


# Create your models here.
class Student(models.Model):
    collage_no = models.IntegerField(primary_key=True)
    name = models.TextField(null=False)
    ph = models.IntegerField(unique=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
