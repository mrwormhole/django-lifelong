from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("services/<>", views.services, name="services"),
    path("academy/", include("blog.urls")),
    path("appointment/", include("appointment.urls")),
    path('master/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)