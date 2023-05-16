
from django.contrib import admin
from django.urls import path,include
from ..films.views import DeleteFilm



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('films.urls')),
    path('',include('accounts.urls')),
    path('films/homepage/<int:pk>/delete/', DeleteFilm.as_view(), name='model_delete'),
    path('__debug__/', include('debug_toolbar.urls')),
]
