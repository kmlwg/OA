from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import UserProfileSignUpForm
from .models import User

# Create your views here.

def index(request):
    return render(request, 'foodUp/index.html')

class UserProfileSignUpView(CreateView):
    model = User
    form_class = UserProfileSignUpForm
    template_name='foodUp/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # TODO narazie dummy, zmienić na inny widok
        return redirect('index')