from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    # return HttpResponse('Welcome to the Moringa Tribune')
    return render(request, 'homepage.html')

# def news_of_day(request):
#     date = dt.date.today()
#     return render(request, 'all-news/today-news.html', {"date": date,})