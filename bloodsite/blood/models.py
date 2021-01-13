from django.conf import settings
from django.db import models
from django.utils import timezone


class Doner(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blood_type = models.CharField(max_length=3)
    birth_date = models.DateTimeField(blank=True, null=True)
    cpf = models.CharField(max_length=11)
    donating_date = models.DateTimeField(default=timezone.now)


class Resource(models.Model):
    type = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    supply = models.IntegerField()