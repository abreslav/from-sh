import pytest
from django.test import TestCase, Client
from django.urls import reverse


class HomeEndpointTestCase(TestCase):
    """Test cases for the home endpoint."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()

    @pytest.mark.timeout(30)
    def test_home_endpoint_success(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.home

        Test that the home endpoint returns a successful response.
        """
        # Test accessing the home endpoint
        response = self.client.get(reverse('home'))

        # Verify the response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello from')
        self.assertContains(response, 'CodeSpeak!')
        self.assertContains(response, 'Welcome to your simple Django web application')

    @pytest.mark.timeout(30)
    def test_home_endpoint_template_used(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.home

        Test that the home endpoint uses the correct template.
        """
        # Test accessing the home endpoint
        response = self.client.get(reverse('home'))

        # Verify the correct template was used
        self.assertTemplateUsed(response, 'home.html')

    @pytest.mark.timeout(30)
    def test_home_endpoint_direct_url(self):
        """
        Test kind: endpoint_tests
        Original method FQN: django_app.views.home

        Test that the home endpoint is accessible via direct URL.
        """
        # Test accessing the home endpoint via direct URL
        response = self.client.get('/')

        # Verify the response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'HelloWorld - CodeSpeak')