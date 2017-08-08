from django.conf.urls import url

from . import views

from . import forms

urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^article/new/$', views.CreateArticleView.as_view(), name = 'article_create'),
    url(r'^article/(?P<pk>\d+)/$', views.ArticleDetailView.as_view(), name = 'article_detail'),
    url(r'^article/(?P<pk>\d+)/update/$', views.UpdateArticleView.as_view(), name = 'article_update'),
   # url(r'^article/(?P<pk>\d+)/add_comment)
]

