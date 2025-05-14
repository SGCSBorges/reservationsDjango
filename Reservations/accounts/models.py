from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('MEMBER', 'Membre'),
        ('AFFILIATE', 'Affilié'),
        ('PRESS', 'Critique'),
        ('PRODUCER', 'Producteur'),
        ('ADMIN', 'Administrateur'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='MEMBER')
    language = models.CharField(max_length=2, default='fr')
    affiliation_code = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"
    
    @property
    def is_affiliate(self):
        return self.role == 'AFFILIATE'
    
    @property
    def is_press(self):
        return self.role == 'PRESS'
    
    @property
    def is_producer(self):
        return self.role == 'PRODUCER'
    

# Get or create profile
# profile = user.userprofile

# Check roles
# if request.user.userprofile.is_affiliate:
    # Affiliate-specific logic

# Get all producers
# from accounts.models import UserProfile
# producers = UserProfile.objects.filter(role='PRODUCER')