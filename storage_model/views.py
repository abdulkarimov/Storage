from django.forms import model_to_dict
from django.http import JsonResponse
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
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

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
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        # Get object with this pk
        category = get_object_or_404(Category.objects.all(), pk=pk)
        category.delete()
        return Response({
            "message": "category with id {} has been deleted.".format(pk)
        }, status=204)


