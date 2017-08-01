from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Article

from .forms import ArticleForm
from django.views.generic.edit import FormView

class ArticleListView(generic.ListView):
	model = Article
	template_name = 'blog/article_list.html'

class ArticleDetailView(generic.DetailView):
	model = Article

def post_article(request):
	form = ArticleForm()
	return render(request, 'blog/article_post.html', {'form' : form})
