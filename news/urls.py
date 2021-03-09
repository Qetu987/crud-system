# from rest_framework import routers
# from .api import NewsViewSet, CommentsViewSet


# router = routers.DefaultRouter()
# router.register('api/news', NewsViewSet, 'news')
# router.register('api/news/<int:pk>', CommentsViewSet, 'comment')



# urlpatterns = router.urls



from django.urls import path
from . import views


urlpatterns = [
    path('api/news/', views.NewsListView.as_view()),
    path('api/news/<int:pk>/', views.CommentsListView.as_view()),
    path('api/news/comments/<int:pk>/', views.CommentsChangeView.as_view())
]