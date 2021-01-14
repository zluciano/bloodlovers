from django.conf import settings
from django.db import models
from django.utils import timezone
from .forms import ResourceForm

danger_supply = 30000

class Doner(models.Model):
    name = models.CharField(max_length=200)
    blood_type = models.CharField(max_length=3)
    birth_date = models.CharField(max_length=10, null=True)
    cpf = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=11)
    donating_date = models.DateTimeField(default=timezone.now)

    def donate(self):
        resource = Resource.objects.get(type=self.blood_type)
        resource.supply += 300
        resource.save()
        self.donating_date = timezone.now()
        self.save()


class Resource(models.Model):
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    supply = models.IntegerField(default=300000)