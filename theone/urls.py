from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("set", views.set_points, name="set_points"),
]
