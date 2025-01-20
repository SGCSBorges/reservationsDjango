from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404

from catalogue.models import Artist
from catalogue.forms import ArtistForm

# Create your views here.
def index(request):
	artists = Artist.objects.all()
	title = 'Liste des artistes'
	
	return render(request, 'artist/index.html', {
		'artists':artists,
		'title':title
	})

def show(request, artist_id):
	try:
		artist = Artist.objects.get(id=artist_id)
	except Artist.DoesNotExist:
		raise Http404('Artist inexistant');
		
	title = 'Fiche d\'un artiste'
	
	return render(request, 'artist/show.html', {
		'artist':artist,
		'title':title 
	})

def create(request):
	title = 'Créer un artiste'
	
	form = ArtistForm(request.POST or None)
	
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('catalogue:artist_index')
	
	return render(request, 'artist/create.html', {
		'form':form,
		'title':title 
	})

def edit(request, artist_id):
	try:
		artist = Artist.objects.get(id=artist_id)
	except Artist.DoesNotExist:
		raise Http404('Artist inexistant');
		
	title = 'Modifier un artiste'

	form = ArtistForm(request.POST or None, instance=artist)
	
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('catalogue:artist_show', artist_id=artist.id)
	
	return render(request, 'artist/edit.html', {
		'form':form,
		'artist':artist,
		'title':title 
	})

def delete(request, artist_id):
	
	artist = get_object_or_404(Artist, id = artist_id)

	if request.method == 'POST':
		artist.delete()
		return redirect('catalogue:artist_index')
	
	return render(request, 'artist/show.html', {
		'artist':artist
	})
