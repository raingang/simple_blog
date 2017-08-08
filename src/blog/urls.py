from django.conf.urls import url

from . import views

from . import forms

urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='article_list'),
    url(r'^article/new/$', views.post_article, name = 'article_form'),
    url(r'^article/(?P<pk>\d+)/$', views.articleDetail, name = 'article_detail'),
    url(r'^article/(?P<pk>\d+)/update/$', views.update_article, name = 'article_update'),
   # url(r'^article/(?P<pk>\d+)/add_comment)
]

