from django.urls import path
from .views import FollowCreateView, FollowDeleteView, FollowingListView, FollowerListView

urlpatterns = [
    path('follows/', FollowCreateView.as_view(), name='follow'),
    path('follows/<int:id>/', FollowDeleteView.as_view(), name='unfollow'),
    path('follows/following/', FollowingListView.as_view(), name='list-following'),
    path('follows/followers/', FollowerListView.as_view(), name='list-followers'),
]