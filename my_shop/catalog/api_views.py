# catalog/api_views.py
# catalog/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Items
from .serializers import ItemsSerializer
from django.shortcuts import get_object_or_404

class ItemListCreateAPIView(APIView):
    def get(self, request):
        items = Items.objects.all()
        serializer = ItemsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Items, pk=pk)

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemsSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
