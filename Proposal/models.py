from django.db import models
from django.utils import timezone


# Create your models here.
class Proposal(models.Model):
    title = models.TextField(null=False)
    proposal = models.BinaryField(null=False)
    accepted = models.BooleanField()
    review_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(null=True)
