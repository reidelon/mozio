from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Provider(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=200)
    language = models.CharField(max_length=5)
    currency = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Polygon(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    geo_data = models.JSONField(null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='service_area')

    def __str__(self):
        return self.name
