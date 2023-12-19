from django.urls import path
from . import views

urlpatterns = [
    # add home urls
    path("", views.home, name="home"),
]
