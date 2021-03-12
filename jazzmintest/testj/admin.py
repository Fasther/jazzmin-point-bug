from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.gis import forms
from django.contrib.gis.db import models

from testj.models import Place


@admin.register(Place)
class PointAdmin(ModelAdmin):
    formfield_overrides = {models.PointField: {"widget": forms.OSMWidget}}
    fieldsets = (
        ("name", {
            "fields": ("name",)
        }),
        ("map", {
            "fields": ("point",)
        }),

    )
