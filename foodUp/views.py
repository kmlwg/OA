from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import Search, Category, MakeComment, SaveFavourite
from users.models import User, Profile, Favourites
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from geopy.geocoders import Nominatim


def home(request):
    return render(request, 'foodUp/home.html')


class PostListView(ListView):
    model = Post
    template_name = 'foodUp/news.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class ProfileDetailView(DetailView):
    template_name = 'foodUp/profile-detail.html'

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=kwargs['pk'])
        form = MakeComment()
        save_form = SaveFavourite()
        com = Comment.objects.filter(receiver_id=kwargs['pk'])

        # Map
        geolocator = Nominatim()
        restaurant = Profile.objects.filter(id=kwargs['pk'])
        name = restaurant[0].name
        address = restaurant[0].adres
        location = geolocator.geocode(address)

        context = {
            'profile': profile,
            'form': form,
            'com': com,
            'save_form': save_form,
            "name": name,
            "lat": location.latitude,
            "lng": location.longitude
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = MakeComment(request.POST)
        save_form = SaveFavourite(request.POST)
        profile = get_object_or_404(Profile, pk=kwargs['pk'])
        com = Comment.objects.filter(receiver_id=kwargs['pk'])
        author = self.request.user
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.sender = author
            new_comment.receiver = profile
            new_comment.save()
        if save_form.is_valid():
            new_fav = save_form.save(commit=False)
            n = Favourites.objects.filter(user=author)
            n = n.filter(profile=profile)
            if n == 'QuerySet []':
                new_fav.user = author
                new_fav.profile = profile
                new_fav.save()
        context = {
            'profile': profile,
            'form': form,
            'com': com,
            'save_form': save_form,
            'n': n
        }
        return render(request, self.template_name, context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'foodUp/new-post.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'foodUp/new-post.html'
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = 'news'
    template_name = 'foodUp/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def search(request):
    my_form = Category()
    if request.method == "POST":
        my_form = Category(request.POST)
        if my_form.is_valid():
            s = my_form.cleaned_data.get('s')
            c = my_form.cleaned_data.get('c')
            r = my_form.cleaned_data.get('r')
            to = my_form.cleaned_data.get('to')

            if s != None:
                profiles = Profile.objects.filter(name__icontains=s)
            else:
                profiles = Profile.objects.all()

            if c:
                f_profiles = []
                for food in c:
                    for p in profiles:
                        if food in p.category:
                            f_profiles.append(p)

                profiles = set(f_profiles)

            if r != None:
                f_profiles = []
                for p in profiles:
                    if p.rate >= r:
                        f_profiles.append(p)

                profiles = f_profiles
            context = {
                'form': my_form,
                'profiles': profiles
            }
    else:
        context = {
            'form': my_form,
            'profiles': Profile.objects.all()
        }
    return render(request, 'foodUp/search.html', context)


def newcompany(request):
    n = Profile.objects.order_by('-pk')[:3]
    context = {
        'n': n
    }
    return render(request, 'foodUp/newcompany.html', context)
