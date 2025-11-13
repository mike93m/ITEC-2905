from django.test import TestCase
from django.urls import reverse

from .models import Place

# Create a test class for testing the homepage
class TestHomePage(TestCase):

    # Test the homepage displays the proper message in no places are in the wishlist 
    def test_load_home_page_shows_empty_for_empty_database(self):
        # The response I expect to get is the home page url
        home_page_url = reverse('place_list')
        response = self.client.get(home_page_url)

        # Ensure the proper view is displayed
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # Ensure the proper text message is displayed when there are no places in the wishlist
        self.assertContains(response, 'You have no places in your travel wishlist.')

class TestWishList(TestCase):

    fixture = ['test_places']

    def test_wishlist_contains_not_visited_places(self):
        response = self.client.get(reverse('place_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertContains(response, 'Tokyo') # This test keeps failing from this line. Not sure why as Ive ensured the spelling is the same as in the json file
        self.assertContains(response, 'New York')
        self.assertNotContains(response, 'San Francisco')
        self.assertNotContains( response, 'Moab')

class TestVisitedList(TestCase):

    fixtures = ['test_places']

    def test_viewing_places_visited_shows_visited_places(self):
        response = self.client.get(reverse('places_visited'))
        self.assertTemplateUsed(response, 'travel_wishlist/visited.html')

        self.assertNotContains(response, 'Tokyo')
        self.assertNotContains(response, 'New York')
        self.assertContains(response, 'San Francisco')        
        self.assertContains(response, 'Moab')

class TestAddNewPlace(TestCase):

    def test_add_new_unvisited_place_to_wishlist(self):

        add_place_url = reverse('place_list')
        new_place_data = {'name': 'Tokyo', 'visited': False }

        # Make a post request to add the new data to the DB
        response = self.client.post(add_place_url, new_place_data, follow=True)
        # Check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # Get the data that populates the template
        response_places = response.context['places']
        # Should be 1 item
        self.assertEqual(1, len(response_places))
        tokyo_response = response_places[0]

        # Verify the item exists in the database 
        tokyo_in_database = Place.objects.get(name='Tokyo', visited=False)

        # Verify the data in the template is the same as the data in the database 
        self.assertEqual(tokyo_in_database, tokyo_response)

        # Same process as above but tries a new place 
        response = self.client.post(reverse('place_list'), { 'name': 'Yosemite', 'visited': False}, follow=True)

        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        response_places = response.context['places']
        # Should be 2 items
        self.assertEqual(2, len(response_places))

        # Verify the places exist in the DB 
        place_in_database = Place.objects.get(name='Yosemite', visited=False)
        place_in_database = Place.objects.get(name='Tokyo', visited=False)

        # Get all the data from the DB 
        places_in_database = Place.objects.all()  # Get all data

        # Ensure DB data is the same as the data rendered in the response 
        self.assertCountEqual(list(places_in_database), list(response_places))


    def test_add_new_visited_place_to_wishlist(self):

        response =  self.client.post(reverse('place_list'), { 'name': 'Tokyo', 'visited': True }, follow=True)

        # Check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # What data was used to populate the template?
        response_places = response.context['places']

        # Should be 0 items - have not added any un-visited places
        self.assertEqual(0, len(response_places))

        # Expect this data to be in the database. Use get() to get data with
        # the values expected. Will throw an exception if no data, or more than
        # one row, matches. Remember throwing an exception will cause this test to fail
        place_in_database = Place.objects.get(name='Tokyo', visited=True)

class TestVisitPlace(TestCase):

    fixtures = ['test_places']

    def test_visit_place(self):

        # visit place pk = 2,  New York
        visit_place_url = reverse('place_was_visited', args=(2, ))
        response = self.client.post(visit_place_url, follow=True)

        # Check correct template was used
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')

        # no New York in the response
        self.assertNotContains(response, 'New York')

        # Is New York visited?
        new_york = Place.objects.get(pk=2)

        self.assertTrue(new_york.visited)


    def test_visit_non_existent_place(self):

        # visit place with pk = 200, this PK is not in the fixtures 
        visit_place_url = reverse('place_was_visited', args=(200, ))
        response = self.client.post(visit_place_url, follow=True)
        self.assertEqual(404, response.status_code)  # not found