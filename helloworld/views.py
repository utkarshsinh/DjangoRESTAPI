from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from helloworld.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostPossessor
from rest_framework import filters
from helloworld.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend

class HelloWorldView(APIView):

    def get(self,request):
        return Response({'message':'Hello World'})
# Create your views here.
class PostView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PostFilter
    ordering_fields =['id']
    search_fields = ['title','content']

    def get_queryset(self):
        return Post.objects.filter(created_by = self.request.user)
# Models into native data types