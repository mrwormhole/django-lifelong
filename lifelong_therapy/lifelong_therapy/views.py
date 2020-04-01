from django.shortcuts import render, redirect

from blog.models import Subscriber, Post

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print(name)

        return redirect("home/index.html")
    latest_post_list = Post.objects.order_by("-published_date")[:3]
    context = {"latest_post_list": latest_post_list}
    return render(request, "home/index.html", context)

def services(request, name):
    context = {"slugName": name}
    return render(request, "home/services.html", context)

def about(request):
    context = {}
    return render(request, "home/about.html", context)

def contact(request):
    context = {}
    return render(request, "home/contact.html", context)

def online_therapy(request):
    context = {}
    return render(request, "home/onlineTherapy.html", context)
