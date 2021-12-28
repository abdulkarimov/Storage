import json
from audioop import reverse

from django.test import TestCase


class ViewTests(TestCase):
    # def test_get_all_products(self):
    #     response = self.client.get('/api/storage/')
    #     self.assertEqual(response.status_code, 200)

    def testPostProduct(self):
        my_json ={
            "Product": {
                "image": "123455.jpeg",
                "name": "88025",
                "price": 25000,
                "count": 3,
            }
        }
        response = self.client.post('http://127.0.0.1:8000/api/storage/',json.dumps(my_json), content_type="application/json" )

        self.assertEqual(response.status_code, 200)