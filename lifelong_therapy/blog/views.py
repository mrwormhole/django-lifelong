from django.shortcuts import render, redirect

from .models import Author, Post, Subscriber

# Get authors and display them
def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        
        # SEND EMAIL HERE
        ###

        subscriber = Subscriber()
        subscriber.subscriber_name = "Anonymous"
        subscriber.subscriber_email = email
        subscriber.save()

        return redirect("home")
    latest_post_list = Post.objects.order_by("-published_date")
    context = {"latest_post_list": latest_post_list}
    return render(request, "blog/index.html", context)

# Show specific author and pots
def detail(request, post_id):
    if request.method == "POST":
        email = request.POST.get("email")
        
        # SEND EMAIL HERE
        ###

        subscriber = Subscriber()
        subscriber.subscriber_name = "Anonymous"
        subscriber.subscriber_email = email
        subscriber.save()

        return redirect("home")
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExists:
        raise Http404("Post does not exist")
    return render(request, "blog/detail.html", { "post": post })
