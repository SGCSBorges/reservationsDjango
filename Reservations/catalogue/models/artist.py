from django.db import models

class Artist(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    biography = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='artists/', null=True, blank=True)
    types = models.ManyToManyField('Type', through='ArtisteType')
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
    class Meta:
        db_table = "artists"
        ordering = ['lastname', 'firstname']
	
