from django.shortcuts import render, redirect
from .forms import UserRegisterForm, EditProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            is_company = form.cleaned_data.get('is_company')
            new_user = authenticate(request, username=form.cleaned_data.get('username'),
                                    password=form.cleaned_data.get('password1'))
            login(request, new_user)

            if is_company:
                return redirect('editprofile')
            else:
                return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def editprofile(request):
    edit_form = EditProfile()
    if request.method == "POST":
        edit_form = EditProfile(request.POST, instance=request.user.profile)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('profile')
    else:
        edit_form = EditProfile(instance=request.user.profile)

    context = {
        'edit_form': edit_form
    }
    return render(request, 'users/editprofile.html', context)
