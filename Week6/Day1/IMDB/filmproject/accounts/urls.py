from django.urls import path
import django.contrib.auth.urls
from .views import Login, SignUp,Profile,LogoutView
from django.contrib.auth import views as auth_views


urlpatterns =[
    path('login/',Login.as_view(),name= 'login'),
    path('signup/',SignUp.as_view()),
    # path('logout/',),
    path('profile/<int:pk>',Profile.as_view(), name='profile'),
    path('logout/',LogoutView.as_view(), name='logout'),

]