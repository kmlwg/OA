from django import forms
from .models import Comment, Post
from users.models import Favourites


class Search(forms.Form):
    s = forms.CharField()
    s1 = forms.CharField(required=False)


class Category(forms.Form):
    OPTIONS = (
        ('pizza', 'pizza'),
        ('beer', 'beer'),
        ('pasta', 'pasta'),
        ('burger', 'burger')
    )
    search = forms.CharField(required=False)
    category = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=OPTIONS)
    rating = forms.DecimalField(required=False)


class MakeComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['com']


class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']


class SaveFavourite(forms.ModelForm):
    class Meta:
        model = Favourites
        exclude = ['user', 'profile']
