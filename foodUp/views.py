from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import Search, Category, MakeComment, SaveFavourite
from users.models import User, Profile, Favourites
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut


def do_geocode(address):
    geolocator = Nominatim()
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        return do_geocode(address)


def home(request):
    n = Profile.objects.order_by('-pk')[:3]
    ratings = []

    for p in n:
        rating = p.ratings.get(object_id=p.id)
        if rating.average > 0:
            ratings.append(rating.average)
        else:
            ratings.append('Not rated')

    profiles = zip(n, ratings)
    context = {
        'profiles': profiles,
    }
    return render(request, 'foodUp/newcompany.html', context)


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
        restaurant = Profile.objects.filter(id=kwargs['pk'])
        name = restaurant[0].name
        address = restaurant[0].adres
        location = do_geocode(address)

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
            form = MakeComment()
        if save_form.is_valid():
            new_fav = save_form.save(commit=False)
            n = Favourites.objects.filter(user=author)
            n = n.filter(profile=profile)
            if n == 'QuerySet []':
                new_fav.user = author
                new_fav.profile = profile
                new_fav.save()

        # Map
        restaurant = Profile.objects.filter(id=kwargs['pk'])
        name = restaurant[0].name
        address = restaurant[0].adres
        location = do_geocode(address)

        context = {
            'profile': profile,
            'form': form,
            'com': com,
            'save_form': save_form,
            "name": name,
            'n': n,
            "lat": location.latitude,
            "lng": location.longitude
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
            s = my_form.cleaned_data.get('search')
            c = my_form.cleaned_data.get('category')
            r = my_form.cleaned_data.get('rating')
            to = my_form.cleaned_data.get('to')
            profiles = Profile.objects.filter(name__icontains=s)

            if c:
                f_profiles = []
                for food in c:
                    for p in profiles:
                        if food in p.category:
                            f_profiles.append(p)

                profiles = set(f_profiles)

            if r != None:
                rated_profiles = profiles.filter(ratings__isnull=False)
                final_profiles = []

                for p in profiles:
                    rating = p.ratings.get(object_id=p.id)
                    avg = rating.average

                    if avg >= r:
                        final_profiles.append(p)

                profiles = final_profiles

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
    ratings = []

    for p in n:
        rating = p.ratings.get(object_id=p.id)
        if rating.average > 0:
            ratings.append(rating.average)
        else:
            ratings.append('Not rated')

    profiles = zip(n, ratings)
    context = {
        'profiles': profiles,
    }
    return render(request, 'foodUp/newcompany.html', context)