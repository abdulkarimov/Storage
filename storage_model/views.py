from apiview.view import APIView
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

from storage_model.models import Product


@permission_classes((permissions.AllowAny,))
class StorageView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = StorageView(instance=product, many=True)
        return Response({"product": serializer.data})