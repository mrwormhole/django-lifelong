from django.shortcuts import render

def home(request):
    context = {"test": "test"}
    return render(request, "home/index.html", context)