from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegisterForm, CompanyRegisterForm

# Create your views here.

def index(request):
    return render(request, 'foodUp/index.html')

def user_register(request):
	form= UserRegisterForm(request.POST or None)
	if form.is_valid():
		form.save(commit=True)
		form= UserRegisterForm()

	context = {
		'form': form
		}
	return render(request, 'foodUp/user_register.html', context)


def company_register(request):
	form= CompanyRegisterForm(request.POST or None)
	if form.is_valid():
		form.save(commit=True)
		form= CompanyRegisterForm()

	context = {
		'form': form
		}
	return render(request, 'foodUp/company_register.html', context)
