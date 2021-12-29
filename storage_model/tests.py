import json
from audioop import reverse

from django.test import TestCase

from storage_model.models import Category, Product


class ViewTests(TestCase):

    def test_get_all_products(self):
        response = self.client.get('/api/storage/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_category(self):
        response = self.client.get('/api/category/')
        self.assertEqual(response.status_code, 200)

    def testPostCategory(self):
        my_json = {
            "Category": {
                "name": "88025",
            }
        }
        response = self.client.post('http://127.0.0.1:8000/api/category/', json.dumps(my_json), content_type="application/json" )
        self.assertTrue(Category.objects.filter(id = response.json()['id']).first())
        self.assertEqual(response.status_code, 200)

    def testPostProduct(self):
        my_json = {"Product":
            {
                "image": "88025",
                "name": "88025",
                "price": 1,
                "count": 1,
                "category_id": 1,
            }
        }
        c = Category(id=1, name="abdulla")
        c.save()

        response = self.client.post('/api/storage/', json.dumps(my_json), content_type="application/json")
        self.assertTrue(Product.objects.filter(id=response.json()['id']).first())
        self.assertEqual(response.status_code, 200)


    def testPutCategory(self):
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




    def testPutProduct(self):
        my_json = {
            "Product": {
                "name": "1010"
            }
        }
        c = Category(id=1,name="qwe")
        c.save()
        p = Product(id=2,image="sss", name="abdulla", price=1, count=1, category=c)
        p.save()

        response = self.client.put('/api/storage/' + str(p.id), json.dumps(my_json), content_type="application/json")
        self.assertTrue(Product.objects.filter(name=response.json()['name']).first())
        self.assertEqual(response.status_code, 200)

    def testDeleteCategory(self):
        c = Category(name="abdulla")
        c.save()
        response = self.client.delete('http://127.0.0.1:8000/api/category/' + str(c.id))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Category.objects.filter(id = c.id).first())

    def testDeleteProduct(self):
        c = Category(id=1, name="qwe")
        c.save()
        p = Product(id=2,image="sss", name="abdulla", price=1, count=1, category=c)
        p.save()

        response = self.client.delete('http://127.0.0.1:8000/api/storage/' + str(p.id))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Product.objects.filter(id=p.id).first())

