"""reservations.catalogue URL Configuration"""

from django.urls import path

from catalogue.views import artist, type, locality, price, show, representation, search_view, about, terms, contact, feed

app_name='catalogue'

urlpatterns = [
    path('artist/', artist.index, name='artist_index'),
    path('artist/<int:artist_id>', artist.show, name='artist_show'),
    path('artist/edit/<int:artist_id>', artist.edit, name='artist_edit'),
    path('artist/create', artist.create, name='artist_create'),
    path('artist/delete/<int:artist_id>', artist.delete, name='artist_delete'),

    path('type/', type.index, name='type_index'),
    path('type/<int:type_id>', type.show, name='type_show'),

    path('locality/', locality.index, name='locality_index'),
    path('locality/<int:locality_id>', locality.show, name='locality_show'),

    path('price/', price.index, name='price_index'),
    path('price/<int:price_id>', price.show, name='price_show'),

    path('show/', show.index, name='show_index'),
    path('show/<int:show_id>', show.show, name='show_show'),

    path('representation/', representation.index, name='representation_index'),
    path('representation/<int:representation_id>', representation.show, name='representation_show'),

    path('search/', search_view.search_view, name='search'),

    path('about/', about.about, name='about'),

    path('terms/', terms.terms, name='terms'),

    path('contact/', contact.contact, name='contact'),

    path('rss/', feed.LatestArtistsFeed(), name='rss_feed'),
]