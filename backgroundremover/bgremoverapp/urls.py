from django.urls import path
from . import views

#Take a look at the urls.py in the root directory
urlpatterns = [
    path("", views.home, name="home"),
]