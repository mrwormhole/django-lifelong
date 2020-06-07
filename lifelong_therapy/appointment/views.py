from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
import pytz
from .models import Therapist, Patient

# Get therapists and display them
def index(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")

        year, month, day = date.split("-")
        year, month, day = int(year), int(month), int(day)
        hour, minute = time.split(":")
        hour, minute = int(hour), int(minute)

        # SEND EMAIL HERE
        import os
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail
        message = Mail(
            from_email='info@lifelongtherapy.com',
            to_emails='lifelonglondon@yandex.com',
            subject='A new person has scheduled an appointment!',
            html_content=('<strong>{} scheduled an appointment at {}, {}. For further details like email and phone number please check the panel.</strong>').format(fullname, time, date))
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        #####

        patient = Patient()
        patient.patient_name = fullname
        patient.patient_email = email
        patient.patient_phone_number = phone
        patient.appointment_date = datetime.datetime(year,month,day,hour,minute,0,tzinfo=pytz.utc)
        patient.therapist = Therapist.objects.all()[0]
        patient.save()

    #therapists_list = Therapist.objects.all
    #context = {"therapists_list": therapists_list}
    context = {}
    return render(request, "appointment/index.html", context)

def appointment_schedule_times(request):
    if request.method == 'GET':
        times_list = []
        selected_date = request.GET["date"]
        year,month,day = selected_date.split("-")
        year, month, day = int(year), int(month), int(day)
        example_therapist = Therapist.objects.all()[:1].get() # Later on therapist names can be selected by user or it will be in administritive order
        patients_on_date = example_therapist.patient_set.all().filter(appointment_date__date=(datetime.date(year,month,day)))
        therapist_time_schedule = [datetime.datetime(year,month,day,i,0,0,tzinfo=pytz.utc) for i in range(9,17)]

        for p in patients_on_date:
            if p.appointment_date in therapist_time_schedule:
                therapist_time_schedule.remove(p.appointment_date)

        for t in therapist_time_schedule:
            times_list.append("{0}:{1}0".format(t.hour,t.minute))
            
        return JsonResponse({
            "schedule_times": times_list
        })
    else:
        return HttpResponse("API doesn't work that way")


