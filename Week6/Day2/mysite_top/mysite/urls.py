from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include('accounts.urls')),
    path("polls/", include('polls.urls')),
    path('polls_rest/', include('rest_framework.urls'))
]
