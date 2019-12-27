from django.db import models
from django.utils import timezone


# Create your models here.
class Research(models.Model):
    title = models.TextField(null=False)
    research = models.BinaryField(null=False)
    date = models.DateTimeField(default=timezone.now)
