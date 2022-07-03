from rest_framework.test import APIRequestFactory, APIClient, APITestCase, force_authenticate

from django.contrib.auth import get_user_model
from django.urls import reverse

from core import views
from core.models import Product, Feedback


User = get_user_model()

class ProductListTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        User.objects.create(username='mike', password='234')
        self.user = User.objects.get(username='mike')

    
    def test_details(self):
        # Test GET request
        request = self.factory.get('api/products/')
        response = views.ProductList.as_view()(request)
        self.assertEqual(response.status_code, 200)

        # Test POST request required fields
        request = self.factory.post('api/products/', {})
        force_authenticate(request, user=self.user)
        response = views.ProductList.as_view()(request)
        self.assertEqual(response.status_code, 400)

        # Test POST request authentication
        request = self.factory.post('api/products/', {"title": "blaaa"})
        response = views.ProductList.as_view()(request)
        self.assertEqual(response.status_code, 403)

        # Success POST
        request = self.factory.post('api/products/', {"title": "hello"})
        force_authenticate(request, user=self.user)
        response = views.ProductList.as_view()(request)
        self.assertEqual(response.status_code, 201)
        product = Product.objects.get(id=1)
        self.assertEqual(product.title, "hello")
