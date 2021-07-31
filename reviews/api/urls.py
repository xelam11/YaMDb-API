from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, ReviewViewSet

router = DefaultRouter()
router.register('', ReviewViewSet, basename='review')
router.register(
    r'(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/titles/<int:title_id>/reviews/', include(router.urls)),
]
