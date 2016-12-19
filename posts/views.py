from django.shortcuts import render
from posts.models import ( Post, 
                           PostAccept, 
                           PostAccepted, 
                           PostRate, 
                           PostSubType, 
                           PostType, 
                           LiveNews, 
                           Tournaments, 
                           Team)
from .services import *


def index(request):  # news also
    context = {}
    #get PAGE INFO, LIVE NEWS
    context = get_base_list().copy()
    # get HOT NEWS
    list_hot_news = get_hot_news()
    context['list_hot_news'] = list_hot_news
    # get TOP 5 
    get_top_five()
    return render(request, 'posts/mainpage.html', context)

def video(request):
    context = {}
    #get PAGE INFO, LIVE NEWS
    context = get_base_list().copy()
    return render(request, 'posts/list_news.html', context)

def gallery(request):
    context = {}
    #get PAGE INFO, LIVE NEWS
    context = get_base_list().copy()
    return render(request, 'posts/list_gallery.html', context)

def list_news(request):
    context = {}
    #get PAGE INFO, LIVE NEWS
    context = get_base_list().copy()
    list_post = PostAccepted.objects.all()
    context['list_post'] = list_post
    return render(request, 'posts/list_news.html', context)

def list_guide(request):
    context = {}
    #get PAGE INFO, LIVE NEWS
    context = get_base_list().copy()
    return render(request, 'posts/list_news.html', context)

def contact(request):
    context = {}
    #get PAGE INFO, LIVE NEWS
    context = get_base_list().copy()
    return render(request, 'posts/contact.html', context)

def single_post(request):
    context = {}
    #get PAGE INFO, LIVE NEWS
    context = get_base_list().copy()
    if "id" in request.GET:
        id = request.GET["id"]
    post = PostAccepted.objects.get(pk=id)
    context['post'] = post
    
    return render(request, 'posts/single_post.html', context)