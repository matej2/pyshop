from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from products import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (
    DetailView,
)
from django.utils.decorators import method_decorator


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect(views.index)
        else:
            messages.success(request, f'Not valid, please check form!')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = User
    template_name = 'profile.html'
