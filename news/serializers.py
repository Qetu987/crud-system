from rest_framework import serializers
from .models import News, Comments

""" сериалайзер для новостей (выводит все) """
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"

""" сериалайзер для комментов (выводит все) """
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
        read_only_fields = ("id", "date", "new")
