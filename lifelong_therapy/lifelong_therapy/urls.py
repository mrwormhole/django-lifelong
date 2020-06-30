from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from . import views

urlpatterns = [
    path("lang/<slug:lang>",views.language_picker, name="language-picker"),
    path("", views.home, name="home"),
    path("online-therapy/", views.online_therapy, name="online-therapy"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("services/<slug:name>", views.services, name="services"),
    path("blog/", include("blog.urls")),
    path("book-appointment/", include("appointment.urls")),
    path('master/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)