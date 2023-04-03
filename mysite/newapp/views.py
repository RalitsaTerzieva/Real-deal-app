from django.shortcuts import render
from .models import Moviedata



def movie_list(request):
    movie_objects = Moviedata.objects.all()
    return render(request, 'newapp/movie_list.html', {'movie_objects': movie_objects})

