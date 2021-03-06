from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Aricle
from .serializers import AricleSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes,permission_classes
# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from  rest_framework.permissions import IsAuthenticated
# @csrf_exempt


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication,BasicAuthentication])
@permission_classes([IsAuthenticated])
def article_list(request):
    def get(self,request,format=None):
        content={
            'user':request.user,
            'auth':request.auth
        }
        return Response(content)
    if request.method == "GET":
        articles = Aricle.objects.all()
        serializer = AricleSerializers(articles, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    elif request.method == "POST":
        # data = JSONParser().parse(request)
        # serializer = AricleSerializers(data=data)
        serializer = AricleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @csrf_exempt


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        article = Aricle.objects.get(pk=pk)
    except Aricle.DoesNotExist:
        # return HttpResponse(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AricleSerializers(article)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    elif request.method == "PUT":
        #data = JSONParser().parse(request)
        serializer = AricleSerializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data)
            return Response(serializer.data)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        article.delete()
        # return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)
