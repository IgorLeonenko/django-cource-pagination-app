from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Moviews

def index(request):
    movies_obj = Moviews.objects.all()

    movie_name  = request.GET.get('movie_name')

    if movie_name != '' and movie_name is not None:
        movies_obj = movies_obj.filter(title_icontains=movie_name)


    paginator = Paginator(movies_obj, 3)
    page = request.GET.get('page')
    movies = paginator.get_page(page)

    return render(request, 'newapp/index.html', {'movies': movies})