from django import forms
from .models import Film, Commercial
from actors.models import Actor

MOVIE_CHOICES = (
    ('FILM', 'Film'),
    ('COMMERCIAL', 'Commercial'),
)

class MovieSelect(forms.Form):
    movie = forms.ChoiceField(choices=MOVIE_CHOICES, label= "", widget=forms.RadioSelect(attrs={'class':'radio_1'}))


class FilmModelForm(forms.ModelForm):
    actor = forms.ModelMultipleChoiceField(label='Actor Select', widget=forms.SelectMultiple, queryset=Actor.objects.filter(is_star=True))
    class Meta:
        model = Film
        fields = '__all__'

class CommercialModelForm(forms.ModelForm):
    actor = forms.ModelMultipleChoiceField(label='Actor Select', widget=forms.SelectMultiple, queryset=Actor.objects.filter(is_star=False))
    class Meta:
        model = Commercial
        fields = '__all__'
