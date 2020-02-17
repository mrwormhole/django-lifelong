from django.shortcuts import render

from .models import Author, Post

# Get authors and display them
def index(request):
    latest_author_list = Author.objects.order_by("-registered_date")
    context = {"latest_author_list": latest_author_list}
    return render(request, "blog/index.html", context)

# Show specific author and pots
def detail(request, author_id):
    try:
        author = Author.objects.get(pk=author_id)
    except Author.DoesNotExists:
        raise Http404("Author does not exist")
    return render(request, "blog/detail.html", { "author": author })
