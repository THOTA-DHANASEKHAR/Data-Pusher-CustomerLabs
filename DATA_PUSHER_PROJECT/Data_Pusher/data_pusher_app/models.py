from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
import requests
from django.urls import reverse

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    email_id = models.EmailField(unique=True)
    account_name = models.CharField(max_length=100)
    app_secret_token = models.CharField(max_length=20, unique=True, blank=True)
    website = models.URLField(blank=True)

@receiver(pre_save, sender=Account)
def generate_app_secret_token(sender, instance, **kwargs):
    if not instance.app_secret_token:
        instance.app_secret_token = get_random_string(length=16)
#---------------Account Done---------------------

class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    http_method = models.CharField(max_length=10)
    headers = models.JSONField()

    def save(self, *args, **kwargs):
        try:
            latest_instance = Destination.objects.latest('id')
            latest_id = latest_instance.id + 1
        except AttributeError:
            latest_id = 1
        except:
            latest_id = 1

        self.url = (self.url) + str(latest_id) +"/"

        if not self.http_method:
            self.http_method = self.detect_http_method()
        super().save(*args, **kwargs)

    def detect_http_method(self):
        try:
            response = requests.options(self.Dest_url)
            return response.headers.get('allow', 'GET').upper()
        except requests.RequestException:
            return 'GET'

#---------------Destination Done---------------------



#http://127.0.0.1:8000/destinations/42/

