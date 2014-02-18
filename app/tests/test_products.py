from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import time

class ProductsTest(APITestCase):

  # Products    
  def test_get_product_200(self):
      """
      check for 200 status from orders
      """
      url = reverse('product-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  def test_create_product(self):
    """
    create a new product
    """
    name = 'product' + str(time.time())
    quantity = 10
    response = self.create_product(name, quantity)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

  def create_product(self, name, quantity):
    url = reverse('product-list');
    data = {
        'name': name,
        'quantity': quantity
    }
    response = self.client.post(url, data, format='json')
    return response

