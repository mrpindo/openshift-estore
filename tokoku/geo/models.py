from django.db import models
from django.forms import ModelForm
from django import forms


class Geoname(models.Model):
    geonameid = models.IntegerField()
    name = models.CharField(max_length=200)
    asciiname = models.CharField(max_length=200)
#    alternatenames = models.CharField(max_length=4000)
    latitude = models.FloatField()
    longitude = models.FloatField()
    fclass = models.CharField(max_length=1)
    fcode = models.CharField(max_length=10)
    country = models.CharField(max_length=2)
    cc2 = models.CharField(max_length=60)
    admin1 = models.CharField(max_length=20)
    admin2 = models.CharField(max_length=80)
    admin3 = models.CharField(max_length=20)
    admin4 = models.CharField(max_length=20)
    #population = models.IntegerField(max_length=10)     #max_lenth ignored if INT in Dajngo 1.8
    population = models.IntegerField(10)
    elevation = models.IntegerField()
    gtopo30 = models.IntegerField()
    timezone = models.CharField(max_length=40)
    modification_date = models.DateTimeField()

    
    def __str__(self):
      return self.name
#the following Meta class is good, temporarily omitted for fast response purpose
#    class Meta:
#      ordering = ['name']


class GeonameForm(ModelForm):
    class Meta:
        model = Geoname
        fields = ('geonameid', 'name',)

