from django.db import models

class ShowArtist(models.Model):
    show = models.ForeignKey('Show', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    role = models.CharField(max_length=100, blank=True)  # e.g., "Lead Actor", "Director"
    
    class Meta:
        db_table = "show_artist"
        unique_together = ('show', 'artist')
