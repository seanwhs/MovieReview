from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Review
from .forms import ReviewForm
# Create your views here.

def home(request):
    
    searchTerm = request.GET.get("searchMovies")
    # If a search term is entered, call the model's filter method 
    # to return the movie objects with a case-insensitive match 
    # to the search term:
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    # If no search term entered, return all movies
    else:
            movies = Movie.objects.all()

    context = {"name":"Sean", "searchTerm":searchTerm, "movies": movies}
    return render(request, "movie/home.html", context)

def about(request):
    context = {}
    return render (request, "movie/about.html", context)

def signup(request):
    email = request.GET.get("email")
    context ={"email":email}
    return render(request, 'movie/signup.html', context)

def call_to_signup(request):
    context = {}
    return render(request, 'movie/call_to_signup.html', context)

def movie_details(request, movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    context = {
        "movie":movie,
        'reviews': reviews,
        }
    return render(request, 'movie/movie_details.html', context)

@login_required
def create_review(request, movie_id):
    # get the movie object from the database
    movie = get_object_or_404(Movie, pk=movie_id)
    # render create_review.html and pass in the review form 
    # for user to create the review
    if request.method == "GET":
        context ={
            'form': ReviewForm,
            'movie': movie,
            }
        return render(request, 'movie/create_review.html', context)
    else:
        try:
            # retrieve the submitted form from the request:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('movie_details', newReview.movie.id)
        # redirect the user back to the movie's detail page. 
        # If there's any error  with the passed-in data, 
        # we render createreview.html again and pass in an error message
        except ValueError:
            context = {
                'form':ReviewForm(),
                'error':'bad data passed in',
            }
            return render(request, 'movie/create_review.html', context)

@login_required
def update_review(request, review_id):
    # We also supply the logged-in user to ensure that other users can't access
    # the review for example, if they manually enter the URL path in the browser.
    # Only the user who created this review can update/delete it.
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        context ={
            'review': review,
            'form':form,
        }
        return render(request, 'movie/update_review.html', context)
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('movie_details', review.movie.id)
        except ValueError:
            context ={
                'review': review,
                'form':form,
                'error':'Bad data in form',
            }
            return render(request, 'movie/update_review.html', context)

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('movie_details', review.movie.id)