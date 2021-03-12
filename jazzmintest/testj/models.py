from django.contrib.gis import forms
from django.contrib.gis.db.models import PointField
from django.db import models

# Create your models here.
from django.db.models import CharField


class Place(models.Model):
    name = CharField(max_length=80)
    point = PointField()

    def __str__(self):
        return self.name


class PlaceForm(forms.Form):
    name = forms.CharField()
    point = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
