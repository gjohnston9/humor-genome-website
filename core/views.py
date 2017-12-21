from django.contrib.auth import login, authenticate, logout as logout_auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Joke

import random


def index(request):
    return render(request, 'core/index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core:view_joke')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout(request):
    logout_auth(request)
    return redirect('core:index')

@login_required
def view_joke(request, joke_id=None):
    if joke_id == None: ### get a random joke_id
        ids = Joke.objects.values_list('joke_id', flat=True)
        joke_id = random.choice(ids)
    joke = get_object_or_404(Joke, pk=joke_id)
    context = {
        'joke': joke,
    }
    return render(request, 'core/view_joke.html', context)

@login_required
def rate(request, joke_id):
    return HttpResponse('You\'re voting on joke {}. Congrats.'.format(joke_id))