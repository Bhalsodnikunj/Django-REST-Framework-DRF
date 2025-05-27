from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')
