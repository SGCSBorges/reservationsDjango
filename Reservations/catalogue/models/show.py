from django.db import models
from django.urls import reverse
from django.utils import timezone

from .location import *
from .artist import *

class Show(models.Model):
    slug = models.CharField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    poster_url = models.CharField(max_length=255, null=True)
    duration = models.PositiveSmallIntegerField(null=True)
    created_in = models.PositiveSmallIntegerField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='shows')
    bookable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    artists = models.ManyToManyField(Artist, through='ShowArtist')
    categories = models.ManyToManyField('Category', blank=True)
    
    def __str__(self):
        return self.title
    
# Add methods for API
    def get_absolute_url(self):
        return reverse('catalogue:show_detail', args=[self.slug])
    
    def upcoming_representations(self):
        return self.representations.filter(schedule__gte=timezone.now())

    class Meta:
        db_table = "shows"