from django.urls import path
from .views import HomePage, MovieSelectView, MovieAddView

app_name = 'movies'
urlpatterns = [
    path('home/', HomePage.as_view(), name='home'),
    path('', MovieSelectView.as_view(), name='select'),
    path('add/', MovieAddView.as_view(), name='add'),
]
