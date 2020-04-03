from django.urls import path

from . import views

app_name = "appointment"

urlpatterns = [
    path("", views.index, name="index"),
    path("appointment_schedule_times/", views.appointment_schedule_times, name="appointment schedule times")
]
