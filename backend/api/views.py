from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets, status
from .models import Movie, Rating
from .serializers import MovieSerializer, MovieMiniSerializer, RatingSerializer
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication,)
    # Read permission unless authenticated
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def list(self, request, *args, **kwargs):
    #     movies = Movie.objects.all()
    #     serializer = MovieMiniSerializer(movies, many=True)
    #     return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:

            movie = Movie.objects.get(id=pk)
            stars = request.data['stars']
            # this is the user based on token identifcation authorization in header
            user = request.user
            
            # below is hardcoded user of id=1
            # user = User.objects.get(id=1)

            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

        else:
            response = {'message': 'you must provide a starts rating between 1 - 5'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class RatingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    # overwrite the default update/create mixins to prevent direct update to the
    # Rating table -- it should be done in the MovieViewSet action method
    def update(self, request, *args, **kwargs):
        response = {'message': "You can't update rating like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': "You can't create rating like that"}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
