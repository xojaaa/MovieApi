from django.urls import path, include
from rest_framework import routers

from .views import MovieViewSet, ActorViewSet, MovieActorAPIView, CommentAPIView, CommentDetailAPIView

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('movies/<int:id>/actors/', MovieActorAPIView.as_view(), name="actors_of_movies"),
   path('comment/', CommentAPIView.as_view(), name="comments"),
   path('comment/<int:id>/', CommentDetailAPIView.as_view(), name="detail-comment")
]

