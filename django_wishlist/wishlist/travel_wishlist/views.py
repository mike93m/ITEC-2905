from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def place_list(request):

    if request.method == "POST":
        form = NewPlaceForm(request.POST)
        place = form.save() # Create a new place from the form data
        if form.is_valid(): # Checks against DB contraints to ensure all required fields are present
            place.save() # Saves the new place to the DB
            return redirect('place_list') # Redirects to get the view with the name place_list which will now show the new place

    # If not a POST request or the form is invalid, render the travel_wishlist page with a blank form to try again
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

@login_required
def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})

@login_required
def place_was_visited(request, place_pk):
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk)
        place.visited = True
        place.save()

    return redirect('place_list')

    