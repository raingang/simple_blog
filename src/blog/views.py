from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Article
from .models import Comment
from django.shortcuts import get_object_or_404
from .forms import ArticleForm
from .forms import CommentForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from django.contrib.auth.models import User
class ArticleListView(generic.ListView):
    model = Article
    template_name = 'blog/article_list.html'

class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

    
def articleDetail(request, pk):
    article = Article.objects.get(pk = pk)
    comments = article.comment_set.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
        	form  = CommentForm(request.POST)
        	if form.is_valid():
        		comment = Comment()
        		comment.title = form.cleaned_data['title']
        		comment.text_content = form.cleaned_data['text_content']
        		comment.author = auth.get_user(request)
        		comment.article = article
        		comment.save()
        else:
        	form = CommentForm()

    else:
        form = None
    return render(request, 'blog/article_detail.html', {'article': article, 'comments' : comments, 'comment_form' : form})



@login_required  # если пользователь не авторизован - редиректит в .../accounts/login
def post_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        print(auth.get_user(request))
        if form.is_valid():            
            article = Article()
            article.title = form.cleaned_data['title']
            article.text_content = form.cleaned_data['text_content']
            article.author = auth.get_user(request)
            article.save()
            return HttpResponseRedirect('/blog')

        else:
        	print('Что-то не так!')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_post.html', {'form': form})


@login_required
def update_article(request, pk):

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog')
    else:
        initial_article = get_object_or_404(Article, pk=pk)
        form = ArticleForm(initial={
            "title": initial_article.title, "text_content": initial_article.text_content})
    return render(request, 'blog/article_update.html', {'form': form})
