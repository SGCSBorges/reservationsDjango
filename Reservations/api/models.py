from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class APIKey(models.Model):
    TIERS = [
        ('FREE', 'Free'),
        ('STARTER', 'Starter'),
        ('PREMIUM', 'Premium'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, unique=True)
    tier = models.CharField(max_length=7, choices=TIERS, default='FREE')
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.tier}"
    
    class Meta:
        verbose_name = "API Key"
        verbose_name_plural = "API Keys"