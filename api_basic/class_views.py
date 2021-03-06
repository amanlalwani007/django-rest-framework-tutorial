from .models import Aricle
from .serializers import AricleSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class ArticleView(APIView):
    def get(self, request, format=None):
        content = {
            'user': (request.user),  # `django.contrib.auth.User` instance.
            'auth': (request.auth),  # None
        }
        return Response(content)
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        articles = Aricle.objects.all()
        serializer = AricleSerializers(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AricleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Aricle.objects.get(pk=pk)
        except Aricle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        articles = self.get_object(pk)
        serializer = AricleSerializers(articles)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = AricleSerializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,formar=None):
        article=self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


