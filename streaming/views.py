from msilib.schema import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import Http404
from streaming.models import Movie
from django.db.models import Avg
from .models import Review
from streaming.models import SubscriptionPlan


def index(request):
    movies = Movie.objects.annotate(
        average=Avg('reviews__rating')
    ).order_by('-average')
    return render(request, 'streaming/index.html', {'movies': movies})


def movie(request, movie_id):
    try:
        print(Movie.objects.get(pk=movie_id))
        movie = Movie.objects.get(pk=movie_id)
        return render(request, 'streaming/movie.html', {'movie': movie})
    except ObjectDoesNotExist:
        raise Http404('Movie not found')


def UserReviewListView(request, user_id):
    reviews = Review.objects.filter(user=user_id)
    return render(request, 'streaming/user_reviews.html', {'reviews': reviews, 'user_id': user_id})


def subscriptionPlan(request, subscription_id):
    movies = Movie.objects.filter(subscription_plans=subscription_id)
    return render(request, "streaming/subscription_plan.html", {'movies': movies, 'subscription_id': subscription_id})
