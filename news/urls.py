from django.urls import path
from . import views


urlpatterns = [
    path('api/news/', views.NewsListView.as_view()),
    path('api/news/<int:pk>/', views.CommentsListView.as_view()),
    path('api/news/comments/<int:pk>/', views.CommentsChangeView.as_view())
]