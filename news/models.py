from django.db import models
from django.urls import reverse

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.CharField(max_length=150)
    author = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    contant = models.CharField(max_length=300)
    new = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.author