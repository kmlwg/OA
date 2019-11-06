from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from foodUp.forms import RegisterForm


def index(request):
    """

    :param request:
    :return:
    """
    return render(request, 'foodUp/index.html')


def register(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'foodUp/register.html', {'form': form})
