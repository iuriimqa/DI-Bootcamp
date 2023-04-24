
from django.contrib import admin
from django.urls import path
from phone_number.views import search_person

urlpatterns = [
    path('admin/', admin.site.urls),
    path("persons/<str:search_value>",search_person),

]
