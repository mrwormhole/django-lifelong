from django.shortcuts import render, redirect

from blog.models import Subscriber

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print(name)

        return redirect("home/index.html")
    context = {}
    return render(request, "home/index.html", context)

def contact(request):
    context = {}
    return render(request, "home/contact.html", context)

# TODO: Finish index of home page

# TODO: Finish contact of home page

#######################################

# TODO: Finish about of home page

# TODO: Finish services of home page????