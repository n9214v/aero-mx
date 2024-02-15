from django.db import models
from mjg_base.classes.log import Log
from django.contrib.auth.models import User
from aero_mx.models.hangar import Hangar

log = Log()


class AircraftCategory(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class AircraftMake(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(AircraftCategory, models.CASCADE, related_name="makes", db_index=True)


class AircraftModel(models.Model):
    title = models.CharField(max_length=30)
    aircraft_make = models.ForeignKey(AircraftMake, models.CASCADE, related_name="models", db_index=True)


class AircraftAttribute(models.Model):
    title = models.CharField(max_length=40)
    category = models.ForeignKey(AircraftCategory, models.CASCADE, related_name="classes", db_index=True)
    creator = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    reviewed = models.CharField(max_length=1, null=True, blank=True)


class Aircraft(models.Model):
    """
    An aircraft belongs to one Hangar, which is owned by a User
    """
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    hangar = models.ForeignKey(Hangar, models.CASCADE, related_name="aircraft", db_index=True)
    aircraft_model = models.ForeignKey(AircraftModel, models.CASCADE, related_name="models", db_index=True)
    year = models.IntegerField(null=True, blank=True)
