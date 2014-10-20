from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from filebrowser.fields import FileBrowseField
from geoposition.fields import GeopositionField

# The Observation model for the Administrative UI for a Field Observation Server.
class Observation(models.Model):
    species = models.CharField(max_length=100, blank=True, null=True)
    family =  models.CharField(max_length=100, blank=True, null=True)
    common_name = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField('Timestamp', auto_now_add=True)
    OBSERVATION_TYPES = (
        ('Stationary', 'Stationary'),
        ('Traveling', 'Traveling'),
        ('Casual', 'Casual'),
        ('Area', 'Area'),
    )
    observation_type = models.CharField(max_length=20, choices=OBSERVATION_TYPES, blank=True, null=True)
    lifeform = models.CharField(max_length=100, blank=True, null=True)
    phenology = models.CharField(max_length=100, blank=True, null=True)
    habitat = models.CharField(max_length=100, blank=True, null=True)
    onserpentine = models.NullBooleanField('On serpentine', blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    gps = GeopositionField("GPS")
    numplants = models.IntegerField('Number of plants', blank=True, null=True)
    image = FileBrowseField("Image", max_length=200, extensions=[".jpg",".png"], blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    revision_notes = models.TextField(max_length=500, blank=True, null=True)
    observername = models.CharField('Observer Name', max_length=100)
    devicename = models.CharField('Device Name', max_length=100, blank=True, null=True)
    edited_by  = models.ForeignKey(User, related_name='edited_by', blank=True, null=True, editable=False)
    edited_on  = models.DateTimeField('Date edited', auto_now=True, blank=True, null=True)
    uploaded = models.BooleanField(default=False)
    validated = models.BooleanField(default=False)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.species
    def was_published_recently(self):
        return self.timestamp >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'timestamp'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
