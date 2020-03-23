from django.shortcuts import render, redirect

from blog.models import Subscriber

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print(name)

        return redirect("home/index.html")
    context = {}
    return render(request, "home/index.html", context)

def services(request):
    context = {}
    return render(request, "home/services.html", context)

def about(request):
    context = {}
    return render(request, "home/about.html", context)

def contact(request):
    context = {}
    return render(request, "home/contact.html", context)
