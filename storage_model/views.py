from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from storage_model.models import Product, Category
from storage_model.serializers import ProductSerializer, CategorySerializer
import json


@permission_classes((permissions.AllowAny,))
class StorageView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(instance=product, many=True)
        return Response({"Product": serializer.data})

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))['Product']
        image = data['image']
        name = data['name']
        price = data['price']
        count = data['count']
        category = data['category_id']
        product = Product(image=image, name=name, price=price, count=count, category=Category.objects.get(id=category))
        product.save()
        return JsonResponse(model_to_dict(product))

    def put(self, request, pk):
        saved_product_method = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data
        serializer = ProductSerializer(instance=saved_product_method, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_product_method = serializer.save()
        return JsonResponse(model_to_dict(saved_product_method))

    def delete(self, request, pk):
        # Get object with this pk
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response({
            "message": "Notification with id {} has been deleted.".format(pk)
        }, status=204)


@permission_classes((permissions.AllowAny,))
class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(instance=category, many=True)
        return Response({"category": serializer.data})

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))['Category']
        name = data['name']

        for i in data:
            if i == 'parent':
                parent = data['parent']
                category = Category(name=name, parent=Category.objects.get(id=parent))
            else:
                category = Category(name=name)

        category.save()
        return JsonResponse(model_to_dict(category))

    def put(self, request, pk):
        category = Category.objects.get(pk=pk)
        data = json.loads(request.body.decode('utf-8'))['Category']
        for i in data:
            if i == 'name':
                name = data['name']
                category.name = name
            if i == 'parent':
                parent = data['parent']
                category.parent = parent
        category.save()
        return JsonResponse(model_to_dict(category))


    def delete(self, request, pk):
            # Get object with this pk
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({
                "message": "category with id {} has been deleted.".format(pk)
            }, status = 204)


@permission_classes((permissions.AllowAny,))
class UpdateCountView(APIView):
    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        data = json.loads(request.body.decode('utf-8'))['Product']
        count = data['count']
        operation = data['operation']

        if operation == "-":
            product.count = product.count - count
        elif operation == "+":
            product.count = product.count + count
        if product.count >= 0:
            product.save()
        else:
            return HttpResponse("count < 0")
        return HttpResponse("message: OK")


@permission_classes((permissions.AllowAny,))
class getProductByIDView(APIView):
    def get(self, request, pk):
        product = Product.objects.filter(pk=pk)
        serializer = ProductSerializer(instance=product, many=True)
        return Response(serializer.data)

