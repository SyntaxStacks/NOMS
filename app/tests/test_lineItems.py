from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import time

class LineItemsTests(APITestCase):

  #Line Items    
  def test_get_lineitem_200(self):
      """
      check for 200 status from orders
      """
      url = reverse('lineitem-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)

