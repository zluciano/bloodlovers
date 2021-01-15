from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


danger_supply = 30000

class Doner(models.Model):
    name = models.CharField(max_length=200)
    blood_type = models.CharField(max_length=3)
    birth_date = models.CharField(max_length=10, null=True)
    cpf = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=11)
    donating_date = models.DateTimeField(default=timezone.now)
    last_notified = models.DateTimeField(default=timezone.now)

    def donate(self):
        resource = Resource.objects.get(type=self.blood_type)
        resource.supply += 300
        resource.save()
        self.donating_date = timezone.now()
        self.last_notified = timezone.now()
        self.save()


class Resource(models.Model):
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    supply = models.IntegerField(default=300000)

    def send_sms(self):
        for doner in Doner.objects.filter(blood_type=self.type).filter(donating_date__lte=timezone.now() - datetime.timedelta(days=90)).filter(last_notified__lte=timezone.now() - datetime.timedelta(days=30)):
            message = client.messages.create(
                            body='Olá, '+doner.name+'! Aqui é do hospital BuserCamp e viemos informar que estamos com o estoque reduzido no seu tipo sanguíneo ('+self.type+'). Encorajamos que retorne para fazer uma nova doação!',
                            from_='+19152098147',
                            to='+55'+doner.phone_number
                        )
            message.sid
            doner.last_notified = timezone.now()
            doner.save()

    def use_blood(self, quantity=30000):
        resource = Resource.objects.get(type=self.type)
        resource.supply -= quantity
        resource.save()
        if self.supply <= danger_supply:
            self.send_sms()
