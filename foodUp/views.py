from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, REDIRECT_FIELD_NAME
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.http import is_safe_url

from .forms import UserProfileSignUpForm, CompanyProfileSignUpForm
from .models import User

# Create your views here.

def index(request):
    return render(request, 'foodUp/index.html')



class UserProfileSignUpView(CreateView):
    '''
    A view for signin up a standard user
    '''
    model = User
    form_class = UserProfileSignUpForm
    template_name='foodUp/signup_form_user.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # TODO narazie dummy, zmienić na inny widok
        return redirect('index')



class CompanyProfileSignUpView(CreateView):
    '''
    A view for signing in a company user
    '''
    model = User
    form_class = CompanyProfileSignUpForm
    template_name='foodUp/signup_form_company.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # TODO narazie dummy, zmienić na inny widok
        return redirect('index')



