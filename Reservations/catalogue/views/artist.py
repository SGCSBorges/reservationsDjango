from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from catalogue.models import Artist
from catalogue.forms import ArtistForm
from reservations.decorators import group_required

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

@login_required
@user_passes_test(lambda u: u.is_staff)
def create(request):
	title = 'Créer un artiste'
	
	form = ArtistForm(request.POST or None)
	
	if request.method == 'POST' and form.is_valid():
		form.save()
		messages.add_message(request, messages.SUCCESS, "Nouvel artiste créé avec succès.")
		return redirect('catalogue:artist_index')
	else:
		messages.add_message(request, messages.ERROR, "Échec de l'ajout d'un nouvel artiste !")

	return render(request, 'artist/create.html', {
		'form':form,
		'title':title 
	})

@login_required
@group_required('ADMIN')
def edit(request, artist_id):
	try:
		artist = Artist.objects.get(id=artist_id)
	except Artist.DoesNotExist:
		raise Http404('Artist inexistant');
		
	title = 'Modifier un artiste'

	form = ArtistForm(request.POST or None, instance=artist)
	
	if request.method == 'POST' and form.is_valid():
		form.save()
		messages.success(request, "Artiste modifié avec succès.")
		return redirect('catalogue:artist_show', artist_id=artist.id)
	else:
		messages.error(request, "Échec de la modification de l'artiste !")
	
	return render(request, 'artist/edit.html', {
		'form':form,
		'artist':artist,
		'title':title 
	})

@login_required
@group_required('ADMIN')
def delete(request, artist_id):
	
	artist = get_object_or_404(Artist, id = artist_id)

	if request.method == 'POST':
		artist.delete()
		messages.success(request, "Artiste supprimé avec succès.")
		return redirect('catalogue:artist_index')
	else:
		messages.error(request, "Échec de la suppression de l'artiste !")
	
	return render(request, 'artist/show.html', {
		'artist':artist
	})
