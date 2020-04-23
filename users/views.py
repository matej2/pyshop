from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from products import views


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect(views.index)
        else:
            messages.success(request, f'Not valid, please check form!')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})