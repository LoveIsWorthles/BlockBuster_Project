from django.shortcuts import render

# Create your views here.
from .models import MovieTheater, MovieTV, News, Slider, SocialLink

def home(request):
    movies = MovieTheater.objects.all()
    tvshows = MovieTV.objects.all()
    news = News.objects.all()
    social_links = SocialLink.objects.all()
    sliders = Slider.objects.all()


    return render(request, "home.html", {
        "movies": movies,
        "tvshows": tvshows,
        "news": news,
        "social_links": social_links,
        "sliders": sliders
    })
