from django.urls import path

from . import views

urlpatterns = [
    path("3/", views.third, name="third"),
    path('show/',views.fourth,name='fourth'),
    path('first/',views.members,name='members')
]