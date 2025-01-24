from django.contrib import admin

from .models import (
    UserMeta,
    Artist,
    Locality,
    Location,
    Price,
    Reservation,
    Show,
    Type,
    ArtisteType,
    Representation,
    RepresentationReservation,
    Review
)

# Register your models here.
admin.site.register(UserMeta)
admin.site.register(Artist)
admin.site.register(Locality)
admin.site.register(Location)
admin.site.register(Price)
admin.site.register(Reservation)
admin.site.register(Show)
admin.site.register(Type)
admin.site.register(ArtisteType)
admin.site.register(Representation)
admin.site.register(RepresentationReservation)
admin.site.register(Review)
