"""reservations.catalogue URL Configuration"""

from django.urls import path

from catalogue import views

app_name='catalogue'

urlpatterns = [
    path('artist/', views.artist.index, name='artist_index'),
    path('artist/<int:artist_id>', views.artist.show, name='artist_show'),
    path('artist/edit/<int:artist_id>', views.artist.edit, name='artist_edit'),
    path('artist/create', views.artist.create, name='artist_create'),
    path('artist/delete/<int:artist_id>', views.artist.delete, name='artist_delete'),
    path('type/', views.type.index, name='type_index'),
    path('type/<int:type_id>', views.type.show, name='type_show'),
    path('locality/', views.locality.index, name='locality_index'),
    path('locality/<int:locality_id>', views.locality.show, name='locality_show'),
    path('price/', views.price.index, name='price_index'),
    path('price/<int:price_id>', views.price.show, name='price_show'),
    path('show/', views.show.index, name='show_index'),
    path('show/<int:show_id>', views.show.show, name='show_show'),
    path('representation/', views.representation.index, name='representation_index'),
    path('representation/<int:representation_id>', views.representation.show, name='representation_show'),
]