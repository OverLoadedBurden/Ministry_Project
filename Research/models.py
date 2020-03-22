from django.db import models
from django.utils import timezone
from users.models import User
from django_serializable_model import SerializableModel


# Create your models here.
class Research(SerializableModel):
    title = models.TextField(null=False)
    date = models.DateTimeField(default=timezone.now)
    research = models.BinaryField(null=True)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.title
