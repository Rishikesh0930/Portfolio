from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def project_page(request):
    return render(request, 'project.html')

def skills_page(request):
    return render(request, 'Skills.html')

def resume_page(request):
    return render(request, 'resume.html')


def contact_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        try:
            send_mail(
                subject=f"{subject}",
                message=f"From: {email}\nName: {name}\n\n{message}",
                from_email=email,
                recipient_list=['rishikeshkushwaha181811@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully.")
            return redirect("contact-page")
        except Exception:
            messages.error(request, "Low internet connection! Please try again.")
    return render(request, 'contact.html')