from django.shortcuts import render

from .models import Therapist, Patient

# Get therapists and display them
def index(request):
    therapists_list = Therapist.objects.all
    context = {"therapists_list": therapists_list}
    return render(request, "appointment/index.html", context)
