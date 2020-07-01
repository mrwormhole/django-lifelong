from django.shortcuts import get_object_or_404, redirect, render

from .models import Author, Post, Subscriber
from django.http import Http404

# Get authors and display them
def index(request):
    if request.method == "POST":
        email = request.POST.get("email")
        
        # SEND EMAIL HERE
        import os
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail
        message = Mail(
            from_email='domain@lifelongtherapy.com',
            to_emails='info@lifelongtherapy.com',
            subject=('A new person{} has subscribed to your newsletter!').format(email),
            html_content='<strong>Make sure to checkout subscribers section in the panel for newly added records.</strong>')
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        #####

        subscriber = Subscriber()
        subscriber.subscriber_name = "Anonymous"
        subscriber.subscriber_email = email
        subscriber.save()

        return redirect("home")
        
    latest_post_list = Post.objects.order_by("-published_date")
    request.session.setdefault("lang", "en")
    lang = request.session["lang"]
    if lang == "tr":
        parentBase = "base_tr.html"
        context = {"lang":lang, "parentBase": parentBase, "latest_post_list": latest_post_list}
    else:
        parentBase = "base.html"
        context = {"lang":lang, "parentBase": parentBase, "latest_post_list": latest_post_list}
    
    return render(request, "blog/index.html", context)

# Show specific author and pots
def detail(request, post_id):
    if request.method == "POST":
        email = request.POST.get("email")
        
        # SEND EMAIL HERE
        import os
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail
        message = Mail(
            from_email='domain@lifelongtherapy.com',
            to_emails='info@lifelongtherapy.com',
            subject=('A new person{} has subscribed to your newsletter!').format(email),
            html_content='<strong>Make sure to checkout subscribers section in the panel for newly added records.</strong>')
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
        ###

        subscriber = Subscriber()
        subscriber.subscriber_name = "Anonymous"
        subscriber.subscriber_email = email
        subscriber.save()

        return redirect("home")
    try:
        # post = Post.objects.get(pk=post_id)
        post = get_object_or_404(Post, pk=post_id)
    except Http404:
        return render(request, "404.html")
    lang = request.session["lang"]
    if lang == "tr":
        parentBase = "base_tr.html"
        context = {"lang":lang, "parentBase": parentBase, "post":post}
    else:
        parentBase = "base.html"
        context = {"lang":lang, "parentBase": parentBase, "post":post}

    return render(request, "blog/detail.html", context)
