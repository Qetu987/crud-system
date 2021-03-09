from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .models import News, Comments
from .serializers import NewsSerializer, CommentsSerializer


"""class for get and post request to news"""
class NewsListView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)

    def post(self, request):
        news = NewsSerializer(data=request.data)
        if news.is_valid():
            news.save()
        return Response(request.data, status=201)


"""class for get and post request to comments and delete, put request to news"""
class CommentsListView(APIView):
    def get(self, request, pk):
        news = News.objects.get(id=pk)
        comments = Comments.objects.filter(new=news)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        request.data["new"] = pk
        serializer = CommentsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def put(self, request, pk):
        try:
            new = News.objects.get(id=pk)
            serializer = NewsSerializer(new, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except News.DoesNotExist:
            return Response(status=404)

    def delete(self, request, pk):
        try:
            new = News.objects.get(id=pk)
        except News.DoesNotExist:
            return Response(status=404)

        try:
            comments = Comments.objects.get(new=pk)
            comments.delete()
        except:
            print("no comments")

        new.delete()
        return Response(status=204)


"""clsdd for put and delete comment"""
class CommentsChangeView(APIView):
    def put(self, request, pk):
        try:
            comm = Comments.objects.get(id=pk)
            serializer = CommentsSerializer(comm, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Comments.DoesNotExist:
            return Response(status=404)

    def delete(self, request, pk):
        try:
            comment = Comments.objects.get(id=pk)
        except Comments.DoesNotExist:
            return Response(status=404)

        comment.delete()
        return Response(status=204)
