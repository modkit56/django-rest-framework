from rest_framework.response import Response
from moviiies_app.models import Movie
from moviiies_app.api.serializers import MovieSerializer
from rest_framework.decorators import api_view

@api_view() # GET is default
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)