from django.db import models
from django.utils import timezone
from users.models import User
from Students.models import *
from django_serializable_model import SerializableModel


# Create your models here.
class Research(SerializableModel):
    title = models.TextField(null=False)
    abstract = models.TextField(null=False)
    degree = models.CharField(null=False, max_length=55)
    date = models.DateTimeField(default=timezone.now)
    std = models.ForeignKey(Student, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unv = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
