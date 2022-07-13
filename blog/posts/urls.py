from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("posts", PostViewSet, basename="posts")

urlpatterns = router.urls

## Endpoints for the generic viewsets
# from .views import PostList, PostDetail, UserList, UserDetail

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
#     path('', PostList.as_view(), name='post_list'),
#     path('users/', UserList.as_view(), name='user_list'),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
# ]