from django.contrib.syndication.views import Feed
from django.urls import reverse
from catalogue.models import Show

class LatestArtistsFeed(Feed):
    title = "Latest Shows"
    link = "/rss/"
    description = "Updates on the latest shows added to the catalog."

    def items(self):
        return Show.objects.order_by('-created_at')[:5]  # Shows the latest 5 shows

    def item_title(self, item):
        return item.title  

    def item_description(self, item):
        return item.description  

    def item_link(self, item):
        return reverse('catalogue:show_show', args=[item.id])  # URL to the show's detail page