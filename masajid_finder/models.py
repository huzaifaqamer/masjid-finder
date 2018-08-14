from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)


class Masjid(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=1000, blank=True, default='')
    latitude = models.FloatField()
    longitude = models.FloatField()
    fajr = models.TimeField()
    zohar = models.TimeField()
    asr = models.TimeField()
    maghrib = models.TimeField()
    isha = models.TimeField()
    jumma = models.TimeField()
    last_modified = models.DateField(auto_now=True)
    contact = models.ManyToManyField(Contact, blank=True)