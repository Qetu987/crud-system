from news.models import News, Comments
from rest_framework import viewsets, permissions
from .serializers import NewsSerializer, CommentsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewsSerializer



# class CommentsViewSet(viewsets.ModelViewSet):
#     news = News.objects.get(id=pk)
#     queryset = Comments.objects.filter(new=news)
#     permissions_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = CommentsSerializer