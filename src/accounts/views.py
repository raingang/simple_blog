

from django.views.generic.edit import FormView
from .models import Profile
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User  # user model
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView

# Для запрета выполнения действий анонимом
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import Http404


def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, prefix="user_form")
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = Profile()
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('/')
    else:
        user_form = UserCreationForm
    return render(request, 'registration/signup.html', {'user_form': user_form})


class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_object(self):
        return User.objects.get(username=self.kwargs.get('username')).profile

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['recent_articles'] = self.get_object().user.article_set.all()[
            :5]
        context['recent_comments'] = self.get_object().user.comment_set.all()[
            :5]
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileDetailView, self).dispatch(request, *args, **kwargs)

'''
@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    recent_articles = user.article_set.all()[:5]
    recent_comments = user.comment_set.all()[:5]
    if request.user == User.objects.get(username=username):
        print('It`s me')
    return render(request, 'registration/profile.html', {"profile": profile, "recent_articles": recent_articles, "recent_comments": recent_comments})
'''


class UpdateProfileView(UpdateView):
    model = Profile
    fields = ['bio', 'location', 'birth_date', 'user_image']
    template_name = 'registration/profile_update.html'
    slug_field = 'username'

    def get_object(self):
        return User.objects.get(username=self.kwargs.get('username')).profile

    def get_success_url(self):
        return reverse('profile', args=[self.kwargs.get('username')])

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        print(dict(self.request.FILES))
        profile = self.get_object()
        if self.request.user != profile.user:
            raise Http404('У вас нет прав редактировать эту запись')
        return super(UpdateProfileView, self).dispatch(request, *args, **kwargs)
