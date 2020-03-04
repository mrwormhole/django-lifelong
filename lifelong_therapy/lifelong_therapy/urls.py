from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/", include("blog.urls")),
    path("appointment/", include("appointment.urls")),
    path('admin/', admin.site.urls)
]
