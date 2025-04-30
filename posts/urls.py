from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikeAPIView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('',include(router.urls)),
    path('posts/<int:post_id>/like/', LikeAPIView.as_view(), name='post-like'),
]