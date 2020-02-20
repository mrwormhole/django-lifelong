from django.urls import path

from . import views

app_name = "appointment"

urlpatterns = [
    path("", appointment.index, name="index"),
]