from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status
import json
import time

class OrdersTest(APITestCase):
  def create_product(self, name, quantity):
    data = {
        'name': name,
        'quantity': quantity
    }
    url = reverse('product-list');
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    return response
  
  def create_line_item(self, name, quantity, productIds):
    data = {
        "product": productIds, 
        "name": "product", 
        "quantity": 0, 
        "value": "12"
    }  
    url = reverse('lineitem-list');
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    return response

  # orders
  def test_get_orders_200(self):
      """
      check for 200 status from orders
      """
      url = reverse('order-list')
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      return response

  def test_create_order(self):
    """
    create order via POST
    """
    productName = 'product' + str(time.time())
    productQuantity = 10
    res = self.create_product(productName, productQuantity)
    res = json.loads(res.content)

    productId = res['id']
    lineItemName = 'product' + str(time.time())
    lineItemQuantity = '1'
    res = self.create_line_item(lineItemName, lineItemQuantity, productId)
    res = json.loads(res.content)
    self.assertEqual(res['id'],1)

    lineItemIds = [ res['id'] ]
    data = {
        'name': 'order' + str(time.time()),
        'vendor': 'seller',
        'customer': 'cust1',
        "lineItems": lineItemIds
    }
    url = reverse('order-list')

    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
