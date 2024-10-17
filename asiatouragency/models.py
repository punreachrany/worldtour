from django.db import models

# Create your models here.

class Tour(models.Model):
    # We need
    # origin country
    # destination
    # number of nights
    # price for that tour

    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_night = models.IntegerField()
    price = models.IntegerField()


