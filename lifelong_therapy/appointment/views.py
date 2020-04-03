from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from .models import Therapist, Patient

# Get therapists and display them
def index(request):
    if request.method == "POST":
        print("submitting appointment")
    therapists_list = Therapist.objects.all
    context = {"therapists_list": therapists_list}
    return render(request, "appointment/index.html", context)

def appointment_schedule_times(request):
    if request.method == 'GET':
        dates_list = []
        selected_date = request.GET["date"]
        year,month,day = selected_date.split("-")
        year, month, day = int(year), int(month), int(day)
        date_first = datetime.date(year,month,day)
        date_second = date_first + datetime.timedelta(days=1)
        example_therapist = Therapist.objects.all()[:1].get()
        patients_on_date = example_therapist.patient_set.all().filter(appointment_date__range=(date_first,date_second))
        
     
        return JsonResponse({
            "schedule_times": [str(),"clown","giraffe"]
        })
    else:
        return HttpResponse("API doesn't work that way")


