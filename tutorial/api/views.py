from rest_framework import viewsets
from .serializers import ApiSerializer
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello, world!</h1>")

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ApiSerializer
