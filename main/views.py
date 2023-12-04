from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.messages import MessageFailure,add_message
from .models import Article,articleSeries


# Create your views here.
def homepage(request):
    matching_series=articleSeries.objects.all()
    return render(request=request,
                  template_name='main/home.html',
                  context={"objects": matching_series}
                  )

def series(request, series: str):
    matching_articles = Article.objects.filter(series__slug=series).all()

    return render(request=request,
                  template_name='main/home.html',
                  context={"objects": matching_articles}
                  )

def article(request, series: str, article: str):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    return render(request=request,
                  template_name='main/article.html',
                  context={"object": matching_article}
                  )
def error(request):
    return render(request=request,
                  template_name='main/error.html',
                  
                  )