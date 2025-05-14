from django.shortcuts import render
from django.db.models import Q
from catalogue.models import Show

def search_view(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    results = []

    if query:
        # Perform a case-insensitive search on the title and description fields
        results = Show.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    context = {
        'query': query,
        'results': results,
        'title': 'Résultats de recherche',
    }
    return render(request, 'search/search_results.html', context)