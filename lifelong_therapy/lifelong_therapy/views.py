from django.shortcuts import render, redirect

from blog.models import Subscriber, Post

def language_picker(request,lang):
    request.session["lang"] = lang
    return redirect("home")

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        # SEND EMAIL HERE
        if (phone[0] == 0 and phone[1] == 7) or (phone[0] == 4 and phone[1] == 4):
            import os
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail
            message = Mail(
                from_email='domain@lifelongtherapy.com',
                to_emails='info@lifelongtherapy.com',
                subject=subject,
                html_content=('<strong>Hi! I am {}. My email is {}, My phone number is {}. Here is my message: {}</strong>').format(name, email, phone, message))
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
            subscriber.subscriber_name = name
            subscriber.subscriber_email = email
            subscriber.subscriber_phone = phone
            subscriber.save()

        return redirect("home")

    latest_post_list = Post.objects.order_by("-published_date")[:3]
    request.session.setdefault("lang", "en")
    lang = request.session["lang"]
    if lang == "tr":
        parentBase = "base_tr.html"
        context = {"lang":lang, "parentBase": parentBase, "latest_post_list": latest_post_list}
    else:
        parentBase = "base.html"
        context = {"lang":lang, "parentBase": parentBase, "latest_post_list": latest_post_list}
    
    return render(request, "home/index.html", context)

def services(request, name):
    lang = request.session["lang"]
    if lang == "tr":
        parentBase = "base_tr.html"
        context = {"lang":lang, "parentBase": parentBase, "slugName": name}
    else:
        parentBase = "base.html"
        context = {"lang":lang, "parentBase": parentBase, "slugName": name}
    return render(request, "home/services.html", context)

def about(request):
    lang = request.session["lang"]
    if lang == "tr":
        parentBase = "base_tr.html"
        context = {"lang":lang, "parentBase": parentBase}
    else:
        parentBase = "base.html"
        context = {"lang":lang, "parentBase": parentBase}
    return render(request, "home/about.html", context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        # SEND EMAIL HERE
        if (len(message) > 44):
            import os
            from sendgrid import SendGridAPIClient
            from sendgrid.helpers.mail import Mail
            message = Mail(
                from_email='domain@lifelongtherapy.com',
                to_emails='info@lifelongtherapy.com',
                subject='A new person has sent a contact information!',
                html_content=('<strong>Hi! I am {}. About the subject:{}, I am sending this message:{}, For further details like email please check the panel.</strong>').format(name, subject, message))
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                # print(response.status_code)
                # print(response.body)
                # print(response.headers)
            except Exception as e:
                print(e.message)
            #####

            subscriber = Subscriber()
            subscriber.subscriber_name = name
            subscriber.subscriber_email = email
            subscriber.save()

        return redirect("home")

    lang = request.session["lang"]
    if lang == "tr":
        parentBase = "base_tr.html"
        context = {"lang":lang, "parentBase": parentBase}
    else:
        parentBase = "base.html"
        context = {"lang":lang, "parentBase": parentBase}
    
    return render(request, "home/contact.html", context)

def online_therapy(request):
    lang = request.session["lang"]
    if lang == "tr":
        parentBase = "base_tr.html"
        context = {"lang":lang, "parentBase": parentBase}
    else:
        parentBase = "base.html"
        context = {"lang":lang, "parentBase": parentBase}
    return render(request, "home/onlineTherapy.html", context)
