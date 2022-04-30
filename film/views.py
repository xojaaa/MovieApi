from django.http import Http404
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Movie, Actor, Comment
from .serializers import MovieSerializer, ActorSerializer, CommentSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ["name", "genre", "actors__name"]
    ordering_fields = ["imdb"]
    filterset_fields = ["genre"]

    @action(detail=True, methods=["DELETE"])
    def delete(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = MovieSerializer(movie)
        movie.delete()
        return Response(serializer.data)

    @action(detail=True, methods=["POST"])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        name = request.data.get("name")
        birtday = request.data.get("birthday")
        gender = request.data.get("gender")
        if name:
            if birtday:
                if gender:
                    actor = Actor.objects.create(name=name, birthday=birtday, gender=gender)
                    movie.actors.add(actor)
                    serializer = ActorSerializer(actor)
                    return Response(data=serializer.data)
        else:
            id = request.data.get("id")
            actor = Actor.objects.get(id=id)
            movie.actors.add(actor)
            serializer = ActorSerializer(actor)
            return Response(data=serializer.data)

    @action(detail=True, methods=["POST"])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        id = request.data.get("id")
        actor = Actor.objects.get(id=id)
        movie.actors.remove(actor)
        serializer = ActorSerializer(actor)
        return Response(serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @action(detail=True, methods=["DELETE"])
    def delete(self, request, *args, **kwargs):
        actor = self.get_object()
        serializer = ActorSerializer(actor)
        actor.delete()
        return Response(serializer.data)


class MovieActorAPIView(APIView):
    def get(self, request, id):
        movie = Movie.objects.get(id=id)
        serializer = ActorSerializer(movie.actors.all(), many=True)
        return Response(serializer.data)


class CommentAPIView(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPIView(APIView):

    def get_object(self, id):
        # Returns an object instance that should
        # be used for detail views.
        try:
            return Comment.objects.get(id=id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, id):
        comment = self.get_object(id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def delete(self, request, id):
        comment = self.get_object(id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        comment = self.get_object(id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        comment = self.get_object(id)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

