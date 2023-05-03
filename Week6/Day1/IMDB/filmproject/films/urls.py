from django.urls import path
from . import views
from .views import Films,AddFilm,AddDirector


urlpatterns = [
    path('films/homepage/',Films.as_view(),name="homepage"),
    path('films/addfilm/', AddFilm.as_view(),name="addfilm"),
    path('films/adddirector/',AddDirector.as_view(),name = "adddirector"),

]