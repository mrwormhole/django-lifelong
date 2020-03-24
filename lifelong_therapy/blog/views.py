from django.shortcuts import render

from .models import Author, Post

# Get authors and display them
def index(request):
    latest_post_list = Post.objects.order_by("-published_date")
    context = {"latest_post_list": latest_post_list}
    return render(request, "blog/index.html", context)

# Show specific author and pots
def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExists:
        raise Http404("Author does not exist")
    return render(request, "blog/detail.html", { "post": post })
