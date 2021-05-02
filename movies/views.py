from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView,TemplateView
from .forms import FilmModelForm, CommercialModelForm, MovieSelect


class MovieSelectView(FormView):
    form_class = MovieSelect
    template_name = 'movies/main.html'
    success_url = reverse_lazy('movies:add')

    def post(self, *args, **kwargs):
        # grabbing what user select and save it to the session with the name movie
        self.request.session['movie'] = self.request.POST.get('movie').lower().capitalize()
        return super().post(*args, **kwargs)


class MovieAddView(FormView):
    template_name = 'movies/add.html'
    success_url = reverse_lazy('movies:home')

    # Taking an action base on the session
    def get_form_class(self, *args, **kwargs):
        movie = self.request.session.get('movie')
        if movie == 'Film':
            return FilmModelForm
        else:
            return CommercialModelForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class HomePage(TemplateView):
    template_name = 'movies/home.html'



    