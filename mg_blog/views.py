from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *


# Create your views here.

def index(request):
    first_news = news.objects.all().latest()
    two_news = news.objects.all()[1:3]
    breaking_news = news.objects.all().latest()
    categories = category.objects.all()[0:4]
    sportnews = news.objects.filter(category='1')
    science_tech = news.objects.filter(category='3')
    politicsnews = news.objects.filter(category='2')[0:4]
    comment_count = comment.objects.all().count()
    all_news = news.objects.all().order_by('-created_at')[0: 4]
    return render(request, 'index.html',
                  {"first_news": first_news, "two_news": two_news, "breaking_news": breaking_news,
                   "all_news": all_news, "categories": categories, 'sportnews': sportnews,
                   'politicsnews': politicsnews, 'science_tech': science_tech, 'comment_count': comment_count})


def news_detail(request, id):
    new = get_object_or_404(news, id=id)
    detail = news.objects.get(id=id)
    comments = comment.objects.filter(news_id=id)

    # form = CommentForm(data=request.POST)
    user_comment = None
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.news = new
            user_comment.save()
            return HttpResponseRedirect("/thanks/")
        else:
            comment_form = CommentForm()

    print(detail)
    return render(request, 'news_detail.html',
                  {'detail': detail, 'comments': comments, 'user_comment': user_comment, 'comment_form': comment_form})


pass
