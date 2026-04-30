from django.shortcuts import render

# Create your views here.
from .models import MovieTheater, MovieTV, News, Slider, SocialLink, Celebrity, Advertisement, Tweet, Trailer, TrailerItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    movies = MovieTheater.objects.all()
    tvshows = MovieTV.objects.all()
    news_qs = News.objects.exclude(section="Newsletter")
    latest_news = news_qs.first()
    more_news = news_qs[1:]
    social_links = SocialLink.objects.all()
    sliders = Slider.objects.all()
    celebrities = Celebrity.objects.all()
    ads = Advertisement.objects.all()
    tweets = Tweet.objects.all()
    trailers = Trailer.objects.all()
    trailer_items = TrailerItem.objects.all()

    return render(request, "home.html", {
        "movies": movies,
        "tvshows": tvshows,
        "latest_news": latest_news,
        "more_news": more_news,
        "social_links": social_links,
        "sliders": sliders,
        "celebrities": celebrities,
        "ads": ads,
        "tweets": tweets,
        "trailers": trailers,
        "trailer_items": trailer_items
    })

@csrf_exempt
def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            News.objects.create(section="Newsletter", title="Subscription", content=email, img_src="", img_alt="", img_width=0, img_height=0, time="")
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'Invalid email'})
    return JsonResponse({'status': 'error'})

def moviesingle(request):
    return render(request, "moviesingle.html")
