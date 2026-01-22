import os
from django.shortcuts import render,redirect
from django.contrib import messages
import requests
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

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

def send_telegram_message(text):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        return False
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }
    try:
        response = requests.post(url, data=payload, timeout=10)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def contact_page(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message", "")
        if not all([name, email, subject, message]):
            messages.error(request, "All fields are required.")
            return redirect("contact-page")
        if (len(name)<3) and (len(name)>30):
            popup_message = "All fields are required."
            messages.error(request, "Name should be between 3 and 30 characters.")
            return redirect("contact-page")
        if email:
            try:
                validate_email(email)
            except ValidationError:
                messages.error(request, "please Enter the valid email address.")
                return redirect("contact-page")
        if len(subject)>100:
            messages.error(request, "Subject should be less than 100 character.")
            return redirect("contact-page")
        if len(message)<30:
            messages.error(request, "Message should be greater than 30 characters.")
            return redirect("contact-page")      
        text =(
        f"📩 <b>Subject - </b>{subject}\n"
        f"📧 <b>Email - </b> {email}\n"
        f"👤 <b>Name - </b> {name}\n\n"
        f"{message}"
        )
        error = send_telegram_message(text)
        if error:
            messages.error(request, "Message sent errorfully!\nIf you don’t receive a reply within 1 hour,\nplease contact me via email.")
        else:
            messages.error(request, "Message failed. Try again later.")
        return redirect("contact-page")
    return render(request, 'contact.html')