from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from .models import Product



User = get_user_model()

class ProductTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(email='user1@user.com')
        cls.product1 = Product.objects.create(
            title = 'produ ct1',
            description = 'this is the description',
            price = '12000',
            discount_price = '20000',
            active = True,
        )


    def test_product_list_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)

    
    def test_product_list_url_by_name(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code,200)

    
    def test_product_title_on_website(self):
        response = self.client.get(reverse('product-list'))
        self.assertContains(response, self.product1.title)

    
    def test_product_detail_url(self):
        response = self.client.get(f'/{self.product1.id}/')
        self.assertEqual(response.status_code,200)

    
    def test_product_detail_by_name(self):
        response = self.client.get(reverse('product-detail', args=[self.product1.id]))
        self.assertEqual(response.status_code,200)

    
    def test_webpage_does_not_exist(self):
        response = self.client.get(reverse('product-detail', args=[999]))
        self.assertEqual(response.status_code, 404)