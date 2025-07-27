

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import SavedMovie
import requests
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

OMDB_API_KEY = '8d64be1e'



def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             messages.success(request, 'Login Successful!!!!')

#             return redirect('index')
#         else:
#             messages.error(request,
#             return redirect('login')
#     return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful!')
            next_url = request.GET.get('next')
            return redirect(next_url if next_url else 'index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



def index(request):
    movie = None
    not_found = False

    if 'movie_name' in request.GET:
        name = request.GET.get('movie_name')
        year = request.GET.get('year')
        url = f"http://www.omdbapi.com/?t={name}&apikey={OMDB_API_KEY}"
        if year:
            url += f"&y={year}"
        response = requests.get(url).json()
        if response.get('Response') == 'True':
            movie = response
        else:
            not_found = True
            messages.warning(request, "Movie not found!")

    return render(request, 'index.html', {'movie': movie, 'not_found': not_found})

@csrf_exempt

@login_required
def save_movie(request):
    if request.method == 'POST':
        categories = request.POST.getlist('category')
        for cat in categories:
            SavedMovie.objects.create(
                user=request.user,
                title=request.POST['title'],
                year=request.POST['year'],
                genre=request.POST['genre'],
                director=request.POST['director'],
                plot=request.POST['plot'],
                poster=request.POST['poster'],
                category=cat
            )
        messages.success(request, "Movie saved successfully!")
    return redirect('index')


@login_required
def saved_movies_all(request):
    movies = SavedMovie.objects.filter(user=request.user).order_by('-saved_at')
    return render(request, 'saved.html', {'movies': movies, 'category': 'All'})

@login_required
def saved_movies(request, category):
    if category == 'all':
        movies = SavedMovie.objects.filter(user=request.user).order_by('-saved_at')
    else:
        movies = SavedMovie.objects.filter(user=request.user, category=category).order_by('-saved_at')
    return render(request, 'saved.html', {'movies': movies, 'category': category})

@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(SavedMovie, id=movie_id, user=request.user)
    movie.delete()
    messages.success(request, 'Movie deleted successfully.')
    return redirect('saved_movies_all')
