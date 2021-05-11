from django.http import Http404
from django.shortcuts import render
from .models import FlashCard, Collection
from .serializers import CardSerializer, CollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class CardList(APIView):

    def get_object(self, pk):
        try:
            return FlashCard.objects.get(pk=pk)
        except FlashCard.DoesNotExist:
            raise Http404

    def get(self, request):
        card = FlashCard.objects.all()
        serializer = CardSerializer(card, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)


class CardDetail(APIView):

    def get_object(self, fk):
        try:
            return FlashCard.objects.filter(collection=fk)
        except FlashCard.DoesNotExist:
            raise Http404


    def get_objectByPK(self, fk):
        try:
            return FlashCard.objects.get(pk=fk)
        except FlashCard.DoesNotExist:
            raise Http404

    def get(self, request, fk):
        product = self.get_object(fk)
        serializer = CardSerializer(product, many=True)
        return Response(serializer.data)

    def delete(self, request, fk):
        card = self.get_objectByPK(fk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, fk):
        card = self.get_objectByPK(fk)
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## lots of junk code in here, will need to come back and clean it up later, lol..

class CollectionList(APIView):

    def get_object(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request):
        card = Collection.objects.all()
        serializer = CollectionSerializer(card, many=True)
        print(card)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)

    def delete(self, request, pk):
        collection = self.get_object(pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CollectionSingle(APIView):

    def get_object(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)

    def delete(self, request, pk):
        collection = self.get_object(pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




