from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Vendor

class VendorAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.vendor = Vendor.objects.create(
            name="Sample Vendor",
            contact_details="Contact Info",
            address="1234 Vendor St",
            vendor_code="VEND123"
        )

    def tearDown(self):
        self.user.delete()
        Vendor.objects.all().delete()
    

    def test_create_vendor(self):
        url = reverse('vendor-list')
        data = {
            "name": "Another Vendor",
            "contact_details": "Another contact detail",
            "address": "4321 New St",
            "vendor_code": "VEND321"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 2)
        self.assertEqual(Vendor.objects.get(id=2).name, "Another Vendor")

    def test_list_vendors(self):
        url = reverse('vendor-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Sample Vendor')
    def test_update_vendor(self):
        url = reverse('vendor-detail', args=[self.vendor.id])
        data = {
            "name": "Updated Vendor",
            "contact_details": "Updated Contact Info",
            "address": "1234 Vendor St",
            "vendor_code": "VEND123"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_vendor = Vendor.objects.get(id=self.vendor.id)
        self.assertEqual(updated_vendor.name, "Updated Vendor")
    def test_delete_vendor(self):
        url = reverse('vendor-detail', args=[self.vendor.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vendor.objects.count(), 0)




