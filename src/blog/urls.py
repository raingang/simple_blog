from django.conf.urls import url

from . import views

from . import forms

urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^article/new/$', views.post_article, name = 'article_form'),
    url(r'^article/(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name = 'article_detail'),
    
]
