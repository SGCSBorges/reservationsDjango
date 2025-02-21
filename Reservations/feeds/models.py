from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class RSSFeed(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    query_params = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('feeds:rss_feed', args=[self.slug])
    
    class Meta:
        verbose_name = "RSS Feed"
        verbose_name_plural = "RSS Feeds"