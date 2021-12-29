import json
from audioop import reverse

from django.test import TestCase

from storage_model.models import Category


class ViewTests(TestCase):

    def test_get_all_products(self):
        response = self.client.get('/api/storage/')
        self.assertEqual(response.status_code, 200)

    def testPostProduct(self):
        my_json = {
            "Category":{
                "name": "88025",
            }
        }
        response = self.client.post('http://127.0.0.1:8000/api/category/', json.dumps(my_json), content_type="application/json" )

        self.assertTrue(Category.objects.filter(id = response.json()['id']).first())
        self.assertEqual(response.status_code, 200)

    def testPutProduct(self):
        my_json = {
            "Category": {
                "name": "1010",
            }
        }
        c = Category(name="abdulla")
        c.save()
        response = self.client.put('http://127.0.0.1:8000/api/category/' + str(c.id), json.dumps(my_json), content_type="application/json")
        self.assertTrue(Category.objects.filter(name="1010").first())
        self.assertEqual(response.status_code, 200)

    def testDeleteProduct(self):
        c = Category(name="abdulla")
        c.save()
        response = self.client.delete('http://127.0.0.1:8000/api/category/' + str(c.id))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Category.objects.filter(id = c.id).first())


