from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products import models
from .serializers import ProductSerializer

# Create your views here.


class ShowProducts(APIView):
    def get(self, request):
        data = models.Product.objects.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)


class RetriveProduct(APIView):
    def get(self, request, id):
        data = get_object_or_404(models.Product, id=id)
        serializer = ProductSerializer(data=data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        data = get_object_or_404(models.Product, id=id)
        serializer = ProductSerializer(instance=data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, id):
        data = get_object_or_404(models.Product, id=id)
        data.delete()
        return Response(status=status.HTTP_200_OK)
