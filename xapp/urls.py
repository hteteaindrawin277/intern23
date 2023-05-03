from django.urls import path

from . import views

urlpatterns = [
    path("2", views.second, name="second"),
]