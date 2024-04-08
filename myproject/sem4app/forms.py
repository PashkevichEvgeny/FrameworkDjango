from django import forms

from sem3app.models import Author, Post


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)


class GameForm(forms.Form):
    name_game = forms.ChoiceField(choices=(('H', 'Head Tails'), ('D', 'Dice'), ('R', 'Rand100')))
    throws = forms.IntegerField(min_value=1, max_value=64)


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'number_post_views']
    author = forms.ChoiceField(choices=((author.pk, author.name) for author in Author.objects.all()))
