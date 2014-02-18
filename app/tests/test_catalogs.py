from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import time

class CatalogTests(APITestCase):

  #Catalogs    
  def test_get_catalog_200(self):
      """
      check for 200 status from orders
      """
      url = reverse('catalog-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
