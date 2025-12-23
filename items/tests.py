from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Item

class ItemAPITestCase(APITestCase):

    def setUp(self):
        # Unique item_code for test DB
        self.item = Item.objects.create(
            item_code="TEST001",
            name="Test Item",
            quantity=10,
            reorder_level=5,
            status="Active"
        )

    # -----------------------
    # CRUD TESTS
    # -----------------------

    def test_get_all_items(self):
        url = reverse('items_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

    def test_get_item_by_id(self):
        url = reverse('item_detail', args=[self.item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['item_code'], "TEST001")

    def test_create_item(self):
        url = reverse('create_item')
        data = {
            "item_code": "TEST002",
            "name": "New Item",
            "quantity": 20,
            "reorder_level": 10,
            "status": "Active"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 2)

    def test_update_item(self):
        url = reverse('update_item', args=[self.item.id])
        data = {
            "item_code": self.item.item_code,
            "name": "Updated Item",
            "quantity": 25,
            "reorder_level": self.item.reorder_level,
            "status": self.item.status
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], 25)

    def test_partial_update_item(self):
        url = reverse('update_item_partial', args=[self.item.id])
        data = {"quantity": 15}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], 15)

    def test_delete_item(self):
        url = reverse('delete_item', args=[self.item.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 0)

    # -----------------------
    # VALIDATION TESTS
    # -----------------------

    def test_create_item_without_name(self):
        url = reverse('create_item')
        data = {
            "item_code": "TEST003",
            "quantity": 5,
            "reorder_level": 2,
            "status": "Active"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_negative_quantity(self):
        url = reverse('create_item')
        data = {
            "item_code": "TEST004",
            "name": "Invalid Item",
            "quantity": -10,
            "reorder_level": 5,
            "status": "Active"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # -----------------------
    # ERROR HANDLING TESTS
    # -----------------------

    def test_get_invalid_item(self):
        url = reverse('item_detail', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_invalid_item(self):
        url = reverse('delete_item', args=[9999])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # -----------------------
    # STATUS CHANGE TESTS
    # -----------------------

    def test_change_status_valid(self):
        url = reverse('change_status', args=[self.item.id])
        data = {"status": "INACTIVE"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], "INACTIVE")

    def test_change_status_invalid(self):
        url = reverse('change_status', args=[self.item.id])
        data = {"status": "INVALID"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
