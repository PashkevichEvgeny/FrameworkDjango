from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)


class GameForm(forms.Form):
    name_game = forms.ChoiceField(choices=(('H', 'Head Tails'), ('D', 'Dice'), ('R', 'Rand100')))
    throws = forms.IntegerField(min_value=1, max_value=64)
