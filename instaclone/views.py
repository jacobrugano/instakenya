from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/accounts/login/')
# Create your views here.
def welcome(request):
    # return HttpResponse('Welcome to the Moringa Tribune')
    return render(request, 'homepage.html')

# def news_of_day(request):
#     date = dt.date.today()
#     return render(request, 'all-news/today-news.html', {"date": date,})

def search_results(request):

    if 'article' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        # searched_articles = Profile.search_by_title(search_term)
        message = f"{search_term}"

        # return render(request, 'search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})