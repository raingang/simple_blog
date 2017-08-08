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

#Views for forms
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

from django.contrib.auth.models import User

# Для запрета выполнения действий анонимом
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ArticleListView(generic.ListView):
    model = Article
    template_name = 'blog/article_list.html'


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.all()
        if self.request.user.is_authenticated():
            context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment()
            comment.title = comment_form.cleaned_data['title']
            comment.text_content = comment_form.cleaned_data['text_content']
            comment.author = auth.get_user(request)
            comment.article = self.get_object()
            comment.save()
        return HttpResponseRedirect('/blog')


'''
def articleDetail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
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
    return render(request, 'blog/article_detail.html', {'article': article, 'comments': comments, 'comment_form': form})
'''
class CreateArticleView(CreateView):
    model = Article
    fields = ['title', 'text_content']
    template_name = 'blog/article_create.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateArticleView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        article = Article()
        article.title = form.cleaned_data['title']
        article.text_content = form.cleaned_data['text_content']
        article.author = auth.get_user(self.request)
        article.save()
        return HttpResponseRedirect('/blog')
'''
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
'''
class UpdateArticleView(UpdateView):
    model = Article
    fields = ['title', 'text_content']
    template_name = 'blog/article_update.html'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UpdateArticleView, self).dispatch(request, *args, **kwargs)
'''
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
'''