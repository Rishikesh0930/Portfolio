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
        try:
            validate_email(email)
        except ValidationError:
            messages.success(request, "Please enter a valid email address.")
        if not all([name, email, subject, message]):
            if not len(name)>3:
                if not len(name)<30:
                    if not len(subject)<100:
                        if not len(message)>30:
                            messages.success(request, "Message should be greater than 30 characters.")
                        messages.success(request, "Subject should be less than 100 character.")
                    messages.success(request, "Name should between 3 and 30 characters.")
                messages.success(request, "Name should between 3 and 30 characters.")
            messages.success(request, "All fields are required.")
        else:
            text =(
            f"📩 <b>Subject - </b>{subject}\n"
            f"📧 <b>Email - </b> {email}\n"
            f"👤 <b>Name - </b> {name}\n\n"
            f"{message}"
            )
            success = send_telegram_message(text)
            if success:
                messages.success(request, "Message sent successfully!\nIf you don’t receive a reply within 1 hour,\nplease contact me via email.")
            else:
                messages.success(request, "Message failed. Try again later.")
            return redirect("contact-page")
    return render(request, 'contact.html')