

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
from .forms import ProfileCreationForm
from django.shortcuts import get_object_or_404


def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, prefix="user_form")
        profile_form = ProfileCreationForm(request.POST, prefix="profile_form")
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = Profile()
            profile.bio = profile_form.cleaned_data.get('bio')
            profile.location = profile_form.cleaned_data.get('location')
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('/')
    else:
        user_form = UserCreationForm()
        profile_form = ProfileCreationForm()
    return render(request, 'registration/signup.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    recent_articles = user.article_set.all()[:5]
    recent_comments = user.comment_set.all()[:5]
    if request.user == User.objects.get(username=username):
        print('It`s me')
    return render(request, 'registration/profile.html', {"profile": profile, "recent_articles": recent_articles, "recent_comments": recent_comments})
