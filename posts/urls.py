from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/', views.list_news, name='list_news'),
    url(r'^guide/', views.list_guide, name='list_guide'),
    url(r'^videos/', views.video, name='video'),
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^post/', views.single_post, name='single_post'),
]