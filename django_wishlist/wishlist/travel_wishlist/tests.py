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
        self.assertContains(response, 'China')
        self.assertContains(response, 'New York')
        self.assertNotContains(response, 'San Francisco')
        self.assertNotContains( response, 'Moab')