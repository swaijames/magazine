from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    first_news = news.objects.all().latest()
    two_news = news.objects.all()[1:3]
    breaking_news = news.objects.all().latest()
    categories = category.objects.all()[0:4]
    sportnews = news.objects.filter(category='1')
    science_tech = news.objects.filter(category='3')
    politicsnews = news.objects.filter(category='2')[0:4]
    # print(sportnews)
    all_news = news.objects.all().order_by('-created_at')[0: 4]
    return render(request, 'index.html',
                  {"first_news": first_news, "two_news": two_news, "breaking_news": breaking_news,
                   "all_news": all_news, "categories": categories, 'sportnews': sportnews,
                   'politicsnews': politicsnews, 'science_tech': science_tech})


def news_detail(request, id):
    detail = news.objects.get(id=id)
    print(detail)
    return render(request, 'news_detail.html', {'detail': detail})
