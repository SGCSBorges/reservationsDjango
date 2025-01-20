"""reservations.catalogue URL Configuration"""

from django.urls import path

from catalogue import views

app_name='catalogue'

urlpatterns = [
    path('artist/', views.artist.index, name='artist_index'),
    path('artist/<int:artist_id>', views.artist.show, name='artist_show'),
    path('artist/edit/<int:artist_id>', views.artist.edit, name='artist_edit'),
    path('artist/create', views.artist.create, name='artist_create'),
]
