from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
from MyPortfolio import settings

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
        Subject = f"{subject}"
        Message = f"Name: {name}\n\n{message}"
        email_from = settings.DEFAULT_FROM_EMAIL 
        recipient_list = [email,'rishikeshkushwaha181811@gmail.com']
        send_mail(Subject, Message, email_from, recipient_list)
        messages.success(request, "Successfull!")
    return render(request, 'contact.html')